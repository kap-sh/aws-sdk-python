"""Generated from Smithy shape ``com.amazonaws.ses#ListConfigurationSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.configuration_sets
    import capo_ses.types.next_token


class ListConfigurationSetsResponse(TypedDict, closed=True):
    configuration_sets: NotRequired[
        "capo_ses.types.configuration_sets.ConfigurationSets"
    ]
    """<p>A list of configuration sets.</p>"""
    next_token: NotRequired["capo_ses.types.next_token.NextToken"]
    """<p>A token indicating that there are additional configuration sets available to be listed. Pass this token to successive calls of <code>ListConfigurationSets</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListConfigurationSetsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "configuration_sets" in value:
        import capo_ses.types.configuration_sets

        capo_ses.types.configuration_sets.serialize_query(
            value["configuration_sets"], pairs, f"{prefix}.ConfigurationSets"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListConfigurationSetsResponse:
    out: ListConfigurationSetsResponse = {}  # type: ignore[typeddict-item]
    child_configuration_sets = el.find("ConfigurationSets")
    if child_configuration_sets is not None:
        import capo_ses.types.configuration_sets

        out["configuration_sets"] = capo_ses.types.configuration_sets.deserialize_query(
            child_configuration_sets
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
