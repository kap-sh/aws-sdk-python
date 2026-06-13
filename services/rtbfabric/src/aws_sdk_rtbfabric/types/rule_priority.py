"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RulePriority``."""

from typing import TypeAlias

"""WAF-style evaluation priority. Lower number = evaluated first (priority 1 before 10). Gaps are allowed (1, 10, 20 is valid). Must be between 1 and 1000 inclusive. Uniqueness per link among non-deleted rules is enforced at the API layer (HTTP 409 on conflict)."""
RulePriority: TypeAlias = int
