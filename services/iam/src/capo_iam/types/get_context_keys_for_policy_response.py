"""Generated from Smithy shape ``com.amazonaws.iam#GetContextKeysForPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.context_key_names_result_list_type


class GetContextKeysForPolicyResponse(TypedDict, closed=True):
    context_key_names: NotRequired[
        "capo_iam.types.context_key_names_result_list_type.ContextKeyNamesResultListType"
    ]
    """<p>The list of context keys that are referenced in the input policies.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetContextKeysForPolicyResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "context_key_names" in value:
        import capo_iam.types.context_key_names_result_list_type

        capo_iam.types.context_key_names_result_list_type.serialize_query(
            value["context_key_names"], pairs, f"{prefix}.ContextKeyNames"
        )


def deserialize_query(el: Element) -> GetContextKeysForPolicyResponse:
    out: GetContextKeysForPolicyResponse = {}  # type: ignore[typeddict-item]
    child_context_key_names = el.find("ContextKeyNames")
    if child_context_key_names is not None:
        import capo_iam.types.context_key_names_result_list_type

        out["context_key_names"] = (
            capo_iam.types.context_key_names_result_list_type.deserialize_query(
                child_context_key_names
            )
        )
    return out
