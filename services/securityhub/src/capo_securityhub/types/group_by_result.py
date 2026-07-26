"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.group_by_values
    import capo_securityhub.types.non_empty_string


class GroupByResult(TypedDict, closed=True):
    group_by_field: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The attribute by which filtered security findings should be grouped.</p>"""
    group_by_values: NotRequired["capo_securityhub.types.group_by_values.GroupByValues"]
    """<p>An array of grouped values and their respective counts for each <code>GroupByField</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupByResult) -> dict:
    out: dict = {}
    if "group_by_field" in value:
        out["GroupByField"] = value["group_by_field"]
    if "group_by_values" in value:
        import capo_securityhub.types.group_by_values

        out["GroupByValues"] = capo_securityhub.types.group_by_values.serialize_json(
            value["group_by_values"]
        )
    return out


def deserialize_json(data: dict) -> GroupByResult:
    out: GroupByResult = {}  # type: ignore[typeddict-item]
    if "GroupByField" in data:
        out["group_by_field"] = data["GroupByField"]
    if "GroupByValues" in data:
        import capo_securityhub.types.group_by_values

        out["group_by_values"] = (
            capo_securityhub.types.group_by_values.deserialize_json(
                data["GroupByValues"]
            )
        )
    return out
