"""Generated from Smithy shape ``com.amazonaws.costexplorer#EC2Specification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.offering_class


class EC2Specification(TypedDict, closed=True):
    offering_class: NotRequired[
        "aws_sdk_cost_explorer.types.offering_class.OfferingClass"
    ]
    """<p>Indicates whether you want a recommendation for standard or convertible reservations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2Specification) -> dict:
    out: dict = {}
    if "offering_class" in value:
        import aws_sdk_cost_explorer.types.offering_class

        out["OfferingClass"] = (
            aws_sdk_cost_explorer.types.offering_class.serialize_aws_json_1_1(
                value["offering_class"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2Specification:
    out: EC2Specification = {}  # type: ignore[typeddict-item]
    if "OfferingClass" in data:
        import aws_sdk_cost_explorer.types.offering_class

        out["offering_class"] = (
            aws_sdk_cost_explorer.types.offering_class.deserialize_aws_json_1_1(
                data["OfferingClass"]
            )
        )
    return out
