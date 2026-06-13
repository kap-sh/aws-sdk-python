"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredModelAlgorithmSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description


class ConfiguredModelAlgorithmSummary(TypedDict):
    create_time: "datetime.datetime"
    """<p>The time at which the configured model algorithm was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured model algorithm was updated.</p>"""
    configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredModelAlgorithmSummary) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ConfiguredModelAlgorithmSummary:
    out: ConfiguredModelAlgorithmSummary = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredModelAlgorithmSummary.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "ConfiguredModelAlgorithmSummary.update_time required"
        )
    if "configuredModelAlgorithmArn" in data:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        raise DeserializationError(
            "ConfiguredModelAlgorithmSummary.configured_model_algorithm_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfiguredModelAlgorithmSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    return out
