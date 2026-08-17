"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EvaluationCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element
from capo_cloudwatch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_prom_ql_criteria


class _EvaluationCriteria_PromQLCriteria(TypedDict, closed=True):
    PromQLCriteria: "capo_cloudwatch.types.alarm_prom_ql_criteria.AlarmPromQLCriteria"


EvaluationCriteria: TypeAlias = _EvaluationCriteria_PromQLCriteria


# --- awsQuery ser/de ---
def serialize_query(
    value: EvaluationCriteria, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "PromQLCriteria" in value:
        import capo_cloudwatch.types.alarm_prom_ql_criteria

        capo_cloudwatch.types.alarm_prom_ql_criteria.serialize_query(
            value["PromQLCriteria"], pairs, f"{prefix}.PromQLCriteria"
        )
    else:
        raise SerializationError("EvaluationCriteria: no variant present")


def deserialize_query(el: Element) -> EvaluationCriteria:
    for child in el:
        if child.tag == "PromQLCriteria":
            import capo_cloudwatch.types.alarm_prom_ql_criteria

            return {
                "PromQLCriteria": capo_cloudwatch.types.alarm_prom_ql_criteria.deserialize_query(
                    child
                )
            }
    raise DeserializationError("EvaluationCriteria: no recognized variant element")


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationCriteria) -> dict:
    if "PromQLCriteria" in value:
        import capo_cloudwatch.types.alarm_prom_ql_criteria

        return {
            "PromQLCriteria": capo_cloudwatch.types.alarm_prom_ql_criteria.serialize_aws_json_1_0(
                value["PromQLCriteria"]
            )
        }
    else:
        raise SerializationError("EvaluationCriteria: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EvaluationCriteria:
    if data.get("PromQLCriteria") is not None:
        import capo_cloudwatch.types.alarm_prom_ql_criteria

        return {
            "PromQLCriteria": capo_cloudwatch.types.alarm_prom_ql_criteria.deserialize_aws_json_1_0(
                data["PromQLCriteria"]
            )
        }
    else:
        raise DeserializationError("EvaluationCriteria: no recognized variant key")
