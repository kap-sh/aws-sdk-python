"""Generated from Smithy shape ``com.amazonaws.shield#SummarizedAttackVector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.string
    import aws_sdk_shield.types.summarized_counter_list


class SummarizedAttackVector(TypedDict, closed=True):
    vector_type: "aws_sdk_shield.types.string.String"
    """<p>The attack type, for example, SNMP reflection or SYN flood.</p>"""
    vector_counters: NotRequired[
        "aws_sdk_shield.types.summarized_counter_list.SummarizedCounterList"
    ]
    """<p>The list of counters that describe the details of the attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummarizedAttackVector) -> dict:
    out: dict = {}
    out["VectorType"] = value["vector_type"]
    if "vector_counters" in value:
        import aws_sdk_shield.types.summarized_counter_list

        out["VectorCounters"] = (
            aws_sdk_shield.types.summarized_counter_list.serialize_aws_json_1_1(
                value["vector_counters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SummarizedAttackVector:
    out: SummarizedAttackVector = {}  # type: ignore[typeddict-item]
    if "VectorType" in data:
        out["vector_type"] = data["VectorType"]
    else:
        raise DeserializationError("SummarizedAttackVector.vector_type required")
    if "VectorCounters" in data:
        import aws_sdk_shield.types.summarized_counter_list

        out["vector_counters"] = (
            aws_sdk_shield.types.summarized_counter_list.deserialize_aws_json_1_1(
                data["VectorCounters"]
            )
        )
    return out
