"""Generated from Smithy shape ``com.amazonaws.ec2#CreationDateCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.maximum_days_since_created_value


class CreationDateCondition(TypedDict):
    maximum_days_since_created: NotRequired[
        "aws_sdk_ec2.types.maximum_days_since_created_value.MaximumDaysSinceCreatedValue"
    ]
    """<p>The maximum number of days that have elapsed since the image was created. For example, a value of <code>300</code> allows images that were created within the last 300 days.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreationDateCondition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maximum_days_since_created" in value:
        pairs.append(
            (
                f"{prefix}.MaximumDaysSinceCreated",
                str(value["maximum_days_since_created"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CreationDateCondition:
    out: CreationDateCondition = {}  # type: ignore[typeddict-item]
    child_maximum_days_since_created = el.find("MaximumDaysSinceCreated")
    if child_maximum_days_since_created is not None:
        out["maximum_days_since_created"] = int(
            child_maximum_days_since_created.text or ""
        )
    return out
