"""Generated from Smithy shape ``com.amazonaws.forecast#Schema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.schema_attributes


class Schema(TypedDict):
    attributes: NotRequired["aws_sdk_forecast.types.schema_attributes.SchemaAttributes"]
    """<p>An array of attributes specifying the name and type of each field in a dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Schema) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_forecast.types.schema_attributes

        out["Attributes"] = (
            aws_sdk_forecast.types.schema_attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Schema:
    out: Schema = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_forecast.types.schema_attributes

        out["attributes"] = (
            aws_sdk_forecast.types.schema_attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out
