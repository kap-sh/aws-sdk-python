"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupVariablesPortSetsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string_list


class RuleGroupVariablesPortSetsDetails(TypedDict, closed=True):
    definition: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The list of port ranges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupVariablesPortSetsDetails) -> dict:
    out: dict = {}
    if "definition" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Definition"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["definition"]
        )
    return out


def deserialize_json(data: dict) -> RuleGroupVariablesPortSetsDetails:
    out: RuleGroupVariablesPortSetsDetails = {}  # type: ignore[typeddict-item]
    if "Definition" in data:
        import capo_securityhub.types.non_empty_string_list

        out["definition"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["Definition"]
            )
        )
    return out
