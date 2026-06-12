"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeSuggestersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.suggester_status_list


class DescribeSuggestersResponse(TypedDict):
    suggesters: "aws_sdk_cloudsearch.types.suggester_status_list.SuggesterStatusList"
    """<p>The suggesters configured for the domain specified in the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSuggestersResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudsearch.types.suggester_status_list

    aws_sdk_cloudsearch.types.suggester_status_list.serialize_query(
        value["suggesters"], pairs, f"{prefix}.Suggesters"
    )


def deserialize_query(el: Element) -> DescribeSuggestersResponse:
    out: DescribeSuggestersResponse = {}  # type: ignore[typeddict-item]
    child_suggesters = el.find("Suggesters")
    if child_suggesters is not None:
        import aws_sdk_cloudsearch.types.suggester_status_list

        out["suggesters"] = (
            aws_sdk_cloudsearch.types.suggester_status_list.deserialize_query(
                child_suggesters
            )
        )
    else:
        raise DeserializationError("DescribeSuggestersResponse.suggesters required")
    return out
