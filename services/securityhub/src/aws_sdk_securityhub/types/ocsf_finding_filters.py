"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfFindingFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.allowed_operators
    import aws_sdk_securityhub.types.composite_filter_list


class OcsfFindingFilters(TypedDict, closed=True):
    composite_filters: NotRequired[
        "aws_sdk_securityhub.types.composite_filter_list.CompositeFilterList"
    ]
    """<p>Enables the creation of complex filtering conditions by combining filter criteria.</p>"""
    composite_operator: NotRequired[
        "aws_sdk_securityhub.types.allowed_operators.AllowedOperators"
    ]
    """<p>The logical operators used to combine the filtering on multiple <code>CompositeFilters</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OcsfFindingFilters) -> dict:
    out: dict = {}
    if "composite_filters" in value:
        import aws_sdk_securityhub.types.composite_filter_list

        out["CompositeFilters"] = (
            aws_sdk_securityhub.types.composite_filter_list.serialize_json(
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


def deserialize_json(data: dict) -> OcsfFindingFilters:
    out: OcsfFindingFilters = {}  # type: ignore[typeddict-item]
    if "CompositeFilters" in data:
        import aws_sdk_securityhub.types.composite_filter_list

        out["composite_filters"] = (
            aws_sdk_securityhub.types.composite_filter_list.deserialize_json(
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
