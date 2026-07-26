"""Generated from Smithy shape ``com.amazonaws.amp#RuleGroupsNamespaceData``."""

import base64
from typing import TypeAlias

"""<p>The rule groups namespace data.</p>"""
RuleGroupsNamespaceData: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupsNamespaceData) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> RuleGroupsNamespaceData:
    return base64.b64decode(data)
