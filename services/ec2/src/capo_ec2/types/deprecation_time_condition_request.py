"""Generated from Smithy shape ``com.amazonaws.ec2#DeprecationTimeConditionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.maximum_days_since_deprecated_value


class DeprecationTimeConditionRequest(TypedDict, closed=True):
    maximum_days_since_deprecated: NotRequired[
        "capo_ec2.types.maximum_days_since_deprecated_value.MaximumDaysSinceDeprecatedValue"
    ]
    """<p>The maximum number of days that have elapsed since the image was deprecated. Set to <code>0</code> to exclude all deprecated images.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprecationTimeConditionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maximum_days_since_deprecated" in value:
        pairs.append(
            (
                f"{prefix}.MaximumDaysSinceDeprecated",
                str(value["maximum_days_since_deprecated"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeprecationTimeConditionRequest:
    out: DeprecationTimeConditionRequest = {}  # type: ignore[typeddict-item]
    child_maximum_days_since_deprecated = el.find("MaximumDaysSinceDeprecated")
    if child_maximum_days_since_deprecated is not None:
        out["maximum_days_since_deprecated"] = int(
            child_maximum_days_since_deprecated.text or ""
        )
    return out
