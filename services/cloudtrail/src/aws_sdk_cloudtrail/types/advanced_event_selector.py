"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AdvancedEventSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.advanced_field_selectors
    import aws_sdk_cloudtrail.types.selector_name


class AdvancedEventSelector(TypedDict, closed=True):
    name: NotRequired["aws_sdk_cloudtrail.types.selector_name.SelectorName"]
    r"""<p>An optional, descriptive name for an advanced event selector, such as \"Log data events for only two S3 buckets\".</p>"""
    field_selectors: (
        "aws_sdk_cloudtrail.types.advanced_field_selectors.AdvancedFieldSelectors"
    )
    """<p>Contains all selector statements in an advanced event selector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedEventSelector) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_cloudtrail.types.advanced_field_selectors

    out["FieldSelectors"] = (
        aws_sdk_cloudtrail.types.advanced_field_selectors.serialize_aws_json_1_1(
            value["field_selectors"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdvancedEventSelector:
    out: AdvancedEventSelector = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "FieldSelectors" in data:
        import aws_sdk_cloudtrail.types.advanced_field_selectors

        out["field_selectors"] = (
            aws_sdk_cloudtrail.types.advanced_field_selectors.deserialize_aws_json_1_1(
                data["FieldSelectors"]
            )
        )
    else:
        raise DeserializationError("AdvancedEventSelector.field_selectors required")
    return out
