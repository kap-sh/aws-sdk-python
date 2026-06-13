"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredAudienceModelOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_destination
    import aws_sdk_cleanroomsml.types.iam_role_arn


class ConfiguredAudienceModelOutputConfig(TypedDict):
    destination: "aws_sdk_cleanroomsml.types.audience_destination.AudienceDestination"
    role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role that can write the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelOutputConfig) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.audience_destination

    out["destination"] = aws_sdk_cleanroomsml.types.audience_destination.serialize_json(
        value["destination"]
    )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> ConfiguredAudienceModelOutputConfig:
    out: ConfiguredAudienceModelOutputConfig = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_cleanroomsml.types.audience_destination

        out["destination"] = (
            aws_sdk_cleanroomsml.types.audience_destination.deserialize_json(
                data["destination"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelOutputConfig.destination required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "ConfiguredAudienceModelOutputConfig.role_arn required"
        )
    return out
