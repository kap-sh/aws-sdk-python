"""Generated from Smithy shape ``com.amazonaws.acm#CommonNameFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_acm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.comparison_operator
    import aws_sdk_acm.types.filter_string


class CommonNameFilter(TypedDict):
    value: "aws_sdk_acm.types.filter_string.FilterString"
    """<p>The value to match against.</p>"""
    comparison_operator: "aws_sdk_acm.types.comparison_operator.ComparisonOperator"
    """<p>The comparison operator to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommonNameFilter) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import aws_sdk_acm.types.comparison_operator

    out["ComparisonOperator"] = (
        aws_sdk_acm.types.comparison_operator.serialize_aws_json_1_1(
            value["comparison_operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CommonNameFilter:
    out: CommonNameFilter = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CommonNameFilter.value required")
    if "ComparisonOperator" in data:
        import aws_sdk_acm.types.comparison_operator

        out["comparison_operator"] = (
            aws_sdk_acm.types.comparison_operator.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    else:
        raise DeserializationError("CommonNameFilter.comparison_operator required")
    return out
