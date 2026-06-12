"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ActionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_recommended_actions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_recommended_actions.types.filter_name
    import aws_sdk_bcm_recommended_actions.types.filter_values
    import aws_sdk_bcm_recommended_actions.types.match_option


class ActionFilter(TypedDict):
    key: "aws_sdk_bcm_recommended_actions.types.filter_name.FilterName"
    """<p>The category to filter on. Valid values are <code>FEATURE</code> for feature type, <code>SEVERITY</code> for severity level, and <code>TYPE</code> for recommendation type.</p>"""
    match_option: "aws_sdk_bcm_recommended_actions.types.match_option.MatchOption"
    """<p>Specifies how to apply the filter. Use <code>EQUALS</code> to include matching results or <code>NOT_EQUALS</code> to exclude matching results.</p>"""
    values: "aws_sdk_bcm_recommended_actions.types.filter_values.FilterValues"
    """<p>One or more values to match against the specified key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionFilter) -> dict:
    out: dict = {}
    import aws_sdk_bcm_recommended_actions.types.filter_name

    out["key"] = (
        aws_sdk_bcm_recommended_actions.types.filter_name.serialize_aws_json_1_0(
            value["key"]
        )
    )
    import aws_sdk_bcm_recommended_actions.types.match_option

    out["matchOption"] = (
        aws_sdk_bcm_recommended_actions.types.match_option.serialize_aws_json_1_0(
            value["match_option"]
        )
    )
    import aws_sdk_bcm_recommended_actions.types.filter_values

    out["values"] = (
        aws_sdk_bcm_recommended_actions.types.filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActionFilter:
    out: ActionFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_bcm_recommended_actions.types.filter_name

        out["key"] = (
            aws_sdk_bcm_recommended_actions.types.filter_name.deserialize_aws_json_1_0(
                data["key"]
            )
        )
    else:
        raise DeserializationError("ActionFilter.key required")
    if "matchOption" in data:
        import aws_sdk_bcm_recommended_actions.types.match_option

        out["match_option"] = (
            aws_sdk_bcm_recommended_actions.types.match_option.deserialize_aws_json_1_0(
                data["matchOption"]
            )
        )
    else:
        raise DeserializationError("ActionFilter.match_option required")
    if "values" in data:
        import aws_sdk_bcm_recommended_actions.types.filter_values

        out["values"] = (
            aws_sdk_bcm_recommended_actions.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        raise DeserializationError("ActionFilter.values required")
    return out
