"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_event_filter_key
    import aws_sdk_ssm.types.ops_item_event_filter_operator
    import aws_sdk_ssm.types.ops_item_event_filter_values


class OpsItemEventFilter(TypedDict):
    key: "aws_sdk_ssm.types.ops_item_event_filter_key.OpsItemEventFilterKey"
    """<p>The name of the filter key. Currently, the only supported value is <code>OpsItemId</code>.</p>"""
    values: "aws_sdk_ssm.types.ops_item_event_filter_values.OpsItemEventFilterValues"
    """<p>The values for the filter, consisting of one or more OpsItem IDs.</p>"""
    operator: (
        "aws_sdk_ssm.types.ops_item_event_filter_operator.OpsItemEventFilterOperator"
    )
    """<p>The operator used by the filter call. Currently, the only supported value is <code>Equal</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventFilter) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.ops_item_event_filter_key

    out["Key"] = aws_sdk_ssm.types.ops_item_event_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import aws_sdk_ssm.types.ops_item_event_filter_values

    out["Values"] = (
        aws_sdk_ssm.types.ops_item_event_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import aws_sdk_ssm.types.ops_item_event_filter_operator

    out["Operator"] = (
        aws_sdk_ssm.types.ops_item_event_filter_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemEventFilter:
    out: OpsItemEventFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_ssm.types.ops_item_event_filter_key

        out["key"] = (
            aws_sdk_ssm.types.ops_item_event_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    else:
        raise DeserializationError("OpsItemEventFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.ops_item_event_filter_values

        out["values"] = (
            aws_sdk_ssm.types.ops_item_event_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("OpsItemEventFilter.values required")
    if "Operator" in data:
        import aws_sdk_ssm.types.ops_item_event_filter_operator

        out["operator"] = (
            aws_sdk_ssm.types.ops_item_event_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("OpsItemEventFilter.operator required")
    return out
