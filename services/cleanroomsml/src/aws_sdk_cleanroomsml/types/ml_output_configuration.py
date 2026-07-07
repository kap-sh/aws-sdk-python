"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MLOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.destination
    import aws_sdk_cleanroomsml.types.iam_role_arn


class MLOutputConfiguration(TypedDict, closed=True):
    destination: NotRequired["aws_sdk_cleanroomsml.types.destination.Destination"]
    """<p>The Amazon S3 location where exported model artifacts are stored.</p>"""
    role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the service access role that is used to store the model artifacts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MLOutputConfiguration) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_cleanroomsml.types.destination

        out["destination"] = aws_sdk_cleanroomsml.types.destination.serialize_json(
            value["destination"]
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> MLOutputConfiguration:
    out: MLOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_cleanroomsml.types.destination

        out["destination"] = aws_sdk_cleanroomsml.types.destination.deserialize_json(
            data["destination"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("MLOutputConfiguration.role_arn required")
    return out
