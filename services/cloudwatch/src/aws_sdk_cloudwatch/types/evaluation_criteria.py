"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EvaluationCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_prom_ql_criteria


class _EvaluationCriteria_PromQLCriteria(TypedDict, closed=True):
    PromQLCriteria: (
        "aws_sdk_cloudwatch.types.alarm_prom_ql_criteria.AlarmPromQLCriteria"
    )


EvaluationCriteria: TypeAlias = _EvaluationCriteria_PromQLCriteria


# --- awsQuery ser/de ---
def serialize_query(
    value: EvaluationCriteria, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "PromQLCriteria" in value:
        import aws_sdk_cloudwatch.types.alarm_prom_ql_criteria

        aws_sdk_cloudwatch.types.alarm_prom_ql_criteria.serialize_query(
            value["PromQLCriteria"], pairs, f"{prefix}.PromQLCriteria"
        )
    else:
        raise SerializationError("EvaluationCriteria: no variant present")


def deserialize_query(el: Element) -> EvaluationCriteria:
    for child in el:
        if child.tag == "PromQLCriteria":
            import aws_sdk_cloudwatch.types.alarm_prom_ql_criteria

            return {
                "PromQLCriteria": aws_sdk_cloudwatch.types.alarm_prom_ql_criteria.deserialize_query(
                    child
                )
            }
    raise DeserializationError("EvaluationCriteria: no recognized variant element")


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationCriteria) -> dict:
    if "PromQLCriteria" in value:
        import aws_sdk_cloudwatch.types.alarm_prom_ql_criteria

        return {
            "PromQLCriteria": aws_sdk_cloudwatch.types.alarm_prom_ql_criteria.serialize_aws_json_1_0(
                value["PromQLCriteria"]
            )
        }
    else:
        raise SerializationError("EvaluationCriteria: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EvaluationCriteria:
    if "PromQLCriteria" in data:
        import aws_sdk_cloudwatch.types.alarm_prom_ql_criteria

        return {
            "PromQLCriteria": aws_sdk_cloudwatch.types.alarm_prom_ql_criteria.deserialize_aws_json_1_0(
                data["PromQLCriteria"]
            )
        }
    else:
        raise DeserializationError("EvaluationCriteria: no recognized variant key")
