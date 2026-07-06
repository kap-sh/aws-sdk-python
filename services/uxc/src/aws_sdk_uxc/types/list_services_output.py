"""Generated from Smithy shape ``com.amazonaws.uxc#ListServicesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_uxc.types.next_token
    import aws_sdk_uxc.types.service_list


class ListServicesOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_uxc.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results. This value is <code>null</code> when no more results are available.</p>"""
    services: NotRequired["aws_sdk_uxc.types.service_list.ServiceList"]
    """<p>The list of available Amazon Web Services service identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "services" in value:
        import aws_sdk_uxc.types.service_list

        out["services"] = aws_sdk_uxc.types.service_list.serialize_json(
            value["services"]
        )
    return out


def deserialize_json(data: dict) -> ListServicesOutput:
    out: ListServicesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "services" in data:
        import aws_sdk_uxc.types.service_list

        out["services"] = aws_sdk_uxc.types.service_list.deserialize_json(
            data["services"]
        )
    return out
