"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTablePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.resource_policy


class GetTablePolicyResponse(TypedDict):
    resource_policy: "aws_sdk_s3tables.types.resource_policy.ResourcePolicy"
    """<p>The <code>JSON</code> that defines the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTablePolicyResponse) -> dict:
    out: dict = {}
    out["resourcePolicy"] = value["resource_policy"]
    return out


def deserialize_json(data: dict) -> GetTablePolicyResponse:
    out: GetTablePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourcePolicy" in data:
        out["resource_policy"] = data["resourcePolicy"]
    else:
        raise DeserializationError("GetTablePolicyResponse.resource_policy required")
    return out
