"""Generated from Smithy shape ``com.amazonaws.mpa#GetPolicyVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policy_version


class GetPolicyVersionResponse(TypedDict):
    policy_version: "aws_sdk_mpa.types.policy_version.PolicyVersion"
    """<p>A <code>PolicyVersion</code> object. Contains details for the version of the policy. Policies define the permissions for team resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyVersionResponse) -> dict:
    out: dict = {}
    import aws_sdk_mpa.types.policy_version

    out["PolicyVersion"] = aws_sdk_mpa.types.policy_version.serialize_json(
        value["policy_version"]
    )
    return out


def deserialize_json(data: dict) -> GetPolicyVersionResponse:
    out: GetPolicyVersionResponse = {}  # type: ignore[typeddict-item]
    if "PolicyVersion" in data:
        import aws_sdk_mpa.types.policy_version

        out["policy_version"] = aws_sdk_mpa.types.policy_version.deserialize_json(
            data["PolicyVersion"]
        )
    else:
        raise DeserializationError("GetPolicyVersionResponse.policy_version required")
    return out
