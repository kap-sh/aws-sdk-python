"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.allowed_operators
    import aws_sdk_securityhub.types.resources_composite_filter_list


class ResourcesFilters(TypedDict):
    composite_filters: NotRequired[
        "aws_sdk_securityhub.types.resources_composite_filter_list.ResourcesCompositeFilterList"
    ]
    """<p>A collection of complex filtering conditions that can be applied to Amazon Web Services resources.</p>"""
    composite_operator: NotRequired[
        "aws_sdk_securityhub.types.allowed_operators.AllowedOperators"
    ]
    """<p>The logical operator used to combine multiple filter conditions in the structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesFilters) -> dict:
    out: dict = {}
    if "composite_filters" in value:
        import aws_sdk_securityhub.types.resources_composite_filter_list

        out["CompositeFilters"] = (
            aws_sdk_securityhub.types.resources_composite_filter_list.serialize_json(
                value["composite_filters"]
            )
        )
    if "composite_operator" in value:
        import aws_sdk_securityhub.types.allowed_operators

        out["CompositeOperator"] = (
            aws_sdk_securityhub.types.allowed_operators.serialize_json(
                value["composite_operator"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourcesFilters:
    out: ResourcesFilters = {}  # type: ignore[typeddict-item]
    if "CompositeFilters" in data:
        import aws_sdk_securityhub.types.resources_composite_filter_list

        out["composite_filters"] = (
            aws_sdk_securityhub.types.resources_composite_filter_list.deserialize_json(
                data["CompositeFilters"]
            )
        )
    if "CompositeOperator" in data:
        import aws_sdk_securityhub.types.allowed_operators

        out["composite_operator"] = (
            aws_sdk_securityhub.types.allowed_operators.deserialize_json(
                data["CompositeOperator"]
            )
        )
    return out
