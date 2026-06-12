"""Generated from Smithy shape ``com.amazonaws.cloud9#UpdateEnvironmentMembershipResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_member


class UpdateEnvironmentMembershipResult(TypedDict):
    membership: NotRequired["aws_sdk_cloud9.types.environment_member.EnvironmentMember"]
    """<p>Information about the environment member whose settings were changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEnvironmentMembershipResult) -> dict:
    out: dict = {}
    if "membership" in value:
        import aws_sdk_cloud9.types.environment_member

        out["membership"] = (
            aws_sdk_cloud9.types.environment_member.serialize_aws_json_1_1(
                value["membership"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEnvironmentMembershipResult:
    out: UpdateEnvironmentMembershipResult = {}  # type: ignore[typeddict-item]
    if "membership" in data:
        import aws_sdk_cloud9.types.environment_member

        out["membership"] = (
            aws_sdk_cloud9.types.environment_member.deserialize_aws_json_1_1(
                data["membership"]
            )
        )
    return out
