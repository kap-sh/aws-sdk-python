"""Generated from Smithy shape ``com.amazonaws.ec2#DeprecationTimeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.maximum_days_since_deprecated_value


class DeprecationTimeCondition(TypedDict, closed=True):
    maximum_days_since_deprecated: NotRequired[
        "capo_ec2.types.maximum_days_since_deprecated_value.MaximumDaysSinceDeprecatedValue"
    ]
    """<p>The maximum number of days that have elapsed since the image was deprecated. When set to <code>0</code>, no deprecated images are allowed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprecationTimeCondition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "maximum_days_since_deprecated" in value:
        pairs.append(
            (
                f"{key_prefix}MaximumDaysSinceDeprecated",
                str(value["maximum_days_since_deprecated"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeprecationTimeCondition:
    out: DeprecationTimeCondition = {}  # type: ignore[typeddict-item]
    child_maximum_days_since_deprecated = el.find("maximumDaysSinceDeprecated")
    if child_maximum_days_since_deprecated is not None:
        out["maximum_days_since_deprecated"] = int(
            child_maximum_days_since_deprecated.text or ""
        )
    return out
