"""Generated from Smithy shape ``com.amazonaws.autoscaling#AlarmSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.alarm_list


class AlarmSpecification(TypedDict, closed=True):
    alarms: NotRequired["capo_auto_scaling.types.alarm_list.AlarmList"]
    """<p>The names of one or more CloudWatch alarms to monitor for the instance refresh. You can specify up to 10 alarms.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AlarmSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarms" in value:
        import capo_auto_scaling.types.alarm_list

        capo_auto_scaling.types.alarm_list.serialize_query(
            value["alarms"], pairs, f"{prefix}.Alarms"
        )


def deserialize_query(el: Element) -> AlarmSpecification:
    out: AlarmSpecification = {}  # type: ignore[typeddict-item]
    child_alarms = el.find("Alarms")
    if child_alarms is not None:
        import capo_auto_scaling.types.alarm_list

        out["alarms"] = capo_auto_scaling.types.alarm_list.deserialize_query(
            child_alarms
        )
    return out
