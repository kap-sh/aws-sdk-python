"""Generated from Smithy shape ``com.amazonaws.glacier#DataRetrievalPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.data_retrieval_rules_list


class DataRetrievalPolicy(TypedDict, closed=True):
    rules: NotRequired[
        "capo_glacier.types.data_retrieval_rules_list.DataRetrievalRulesList"
    ]
    """<p>The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataRetrievalPolicy) -> dict:
    out: dict = {}
    if "rules" in value:
        import capo_glacier.types.data_retrieval_rules_list

        out["Rules"] = capo_glacier.types.data_retrieval_rules_list.serialize_json(
            value["rules"]
        )
    return out


def deserialize_json(data: dict) -> DataRetrievalPolicy:
    out: DataRetrievalPolicy = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import capo_glacier.types.data_retrieval_rules_list

        out["rules"] = capo_glacier.types.data_retrieval_rules_list.deserialize_json(
            data["Rules"]
        )
    return out
