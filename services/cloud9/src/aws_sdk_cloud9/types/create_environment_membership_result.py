"""Generated from Smithy shape ``com.amazonaws.cloud9#CreateEnvironmentMembershipResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_member


class CreateEnvironmentMembershipResult(TypedDict, closed=True):
    membership: "aws_sdk_cloud9.types.environment_member.EnvironmentMember"
    """<p>Information about the environment member that was added.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEnvironmentMembershipResult) -> dict:
    out: dict = {}
    import aws_sdk_cloud9.types.environment_member

    out["membership"] = aws_sdk_cloud9.types.environment_member.serialize_aws_json_1_1(
        value["membership"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEnvironmentMembershipResult:
    out: CreateEnvironmentMembershipResult = {}  # type: ignore[typeddict-item]
    if "membership" in data:
        import aws_sdk_cloud9.types.environment_member

        out["membership"] = (
            aws_sdk_cloud9.types.environment_member.deserialize_aws_json_1_1(
                data["membership"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEnvironmentMembershipResult.membership required"
        )
    return out
