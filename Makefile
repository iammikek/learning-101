.PHONY: sync update status

# Check out the commits recorded in this repo
sync:
	git submodule update --init --recursive

# Fast-forward each submodule to origin/main (does not commit pins)
update:
	git submodule foreach 'git fetch origin && git checkout main && git pull --ff-only origin main || true'

status:
	git submodule status
