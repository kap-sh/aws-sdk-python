"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AdvancedEventSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.field_selectors


class AdvancedEventSelector(TypedDict):
    name: NotRequired["str"]
    """<p>An optional, descriptive name for an advanced event selector, such as \"Log data events for only two S3 buckets\".</p>"""
    field_selectors: "aws_sdk_observabilityadmin.types.field_selectors.FieldSelectors"
    """<p>Contains all selector statements in an advanced event selector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedEventSelector) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_observabilityadmin.types.field_selectors

    out["FieldSelectors"] = (
        aws_sdk_observabilityadmin.types.field_selectors.serialize_json(
            value["field_selectors"]
        )
    )
    return out


def deserialize_json(data: dict) -> AdvancedEventSelector:
    out: AdvancedEventSelector = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "FieldSelectors" in data:
        import aws_sdk_observabilityadmin.types.field_selectors

        out["field_selectors"] = (
            aws_sdk_observabilityadmin.types.field_selectors.deserialize_json(
                data["FieldSelectors"]
            )
        )
    else:
        raise DeserializationError("AdvancedEventSelector.field_selectors required")
    return out
