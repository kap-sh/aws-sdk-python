"""Generated from Smithy shape ``com.amazonaws.ec2#CreationDateConditionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.maximum_days_since_created_value


class CreationDateConditionRequest(TypedDict, closed=True):
    maximum_days_since_created: NotRequired[
        "capo_ec2.types.maximum_days_since_created_value.MaximumDaysSinceCreatedValue"
    ]
    """<p>The maximum number of days that have elapsed since the image was created. For example, a value of <code>300</code> allows images that were created within the last 300 days.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreationDateConditionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maximum_days_since_created" in value:
        pairs.append(
            (
                f"{prefix}.MaximumDaysSinceCreated",
                str(value["maximum_days_since_created"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CreationDateConditionRequest:
    out: CreationDateConditionRequest = {}  # type: ignore[typeddict-item]
    child_maximum_days_since_created = el.find("MaximumDaysSinceCreated")
    if child_maximum_days_since_created is not None:
        out["maximum_days_since_created"] = int(
            child_maximum_days_since_created.text or ""
        )
    return out
