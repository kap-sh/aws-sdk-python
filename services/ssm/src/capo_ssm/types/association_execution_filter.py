"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.association_execution_filter_key
    import capo_ssm.types.association_execution_filter_value
    import capo_ssm.types.association_filter_operator_type


class AssociationExecutionFilter(TypedDict, closed=True):
    key: "capo_ssm.types.association_execution_filter_key.AssociationExecutionFilterKey"
    """<p>The key value used in the request.</p>"""
    value: "capo_ssm.types.association_execution_filter_value.AssociationExecutionFilterValue"
    """<p>The value specified for the key.</p>"""
    type: (
        "capo_ssm.types.association_filter_operator_type.AssociationFilterOperatorType"
    )
    """<p>The filter type specified in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.association_execution_filter_key

    out["Key"] = capo_ssm.types.association_execution_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    out["Value"] = value["value"]
    import capo_ssm.types.association_filter_operator_type

    out["Type"] = (
        capo_ssm.types.association_filter_operator_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationExecutionFilter:
    out: AssociationExecutionFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.association_execution_filter_key

        out["key"] = (
            capo_ssm.types.association_execution_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    else:
        raise DeserializationError("AssociationExecutionFilter.key required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("AssociationExecutionFilter.value required")
    if data.get("Type") is not None:
        import capo_ssm.types.association_filter_operator_type

        out["type"] = (
            capo_ssm.types.association_filter_operator_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("AssociationExecutionFilter.type required")
    return out
