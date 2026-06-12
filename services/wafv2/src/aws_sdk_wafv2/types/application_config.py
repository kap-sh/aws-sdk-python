"""Generated from Smithy shape ``com.amazonaws.wafv2#ApplicationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.application_attributes


class ApplicationConfig(TypedDict):
    attributes: NotRequired[
        "aws_sdk_wafv2.types.application_attributes.ApplicationAttributes"
    ]
    """<p>Contains the attribute name and a list of values for that attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationConfig) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_wafv2.types.application_attributes

        out["Attributes"] = (
            aws_sdk_wafv2.types.application_attributes.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationConfig:
    out: ApplicationConfig = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_wafv2.types.application_attributes

        out["attributes"] = (
            aws_sdk_wafv2.types.application_attributes.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    return out
