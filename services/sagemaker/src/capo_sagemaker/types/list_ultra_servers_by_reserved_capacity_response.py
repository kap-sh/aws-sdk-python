"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListUltraServersByReservedCapacityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.ultra_servers


class ListUltraServersByReservedCapacityResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. Use it in the next request to retrieve the next set of UltraServers.</p>"""
    ultra_servers: NotRequired["capo_sagemaker.types.ultra_servers.UltraServers"]
    """<p>A list of UltraServers that are part of the specified reserved capacity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUltraServersByReservedCapacityResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "ultra_servers" in value:
        import capo_sagemaker.types.ultra_servers

        out["UltraServers"] = capo_sagemaker.types.ultra_servers.serialize_aws_json_1_1(
            value["ultra_servers"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUltraServersByReservedCapacityResponse:
    out: ListUltraServersByReservedCapacityResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "UltraServers" in data:
        import capo_sagemaker.types.ultra_servers

        out["ultra_servers"] = (
            capo_sagemaker.types.ultra_servers.deserialize_aws_json_1_1(
                data["UltraServers"]
            )
        )
    return out
