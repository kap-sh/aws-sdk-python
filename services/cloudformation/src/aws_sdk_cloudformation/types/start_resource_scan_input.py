"""Generated from Smithy shape ``com.amazonaws.cloudformation#StartResourceScanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.client_request_token
    import aws_sdk_cloudformation.types.scan_filters


class StartResourceScanInput(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for this <code>StartResourceScan</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to start a new resource scan.</p>"""
    scan_filters: NotRequired["aws_sdk_cloudformation.types.scan_filters.ScanFilters"]
    """<p>The scan filters to use.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartResourceScanInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_request_token" in value:
        pairs.append(
            (f"{prefix}.ClientRequestToken", str(value["client_request_token"]))
        )
    if "scan_filters" in value:
        import aws_sdk_cloudformation.types.scan_filters

        aws_sdk_cloudformation.types.scan_filters.serialize_query(
            value["scan_filters"], pairs, f"{prefix}.ScanFilters"
        )


def deserialize_query(el: Element) -> StartResourceScanInput:
    out: StartResourceScanInput = {}  # type: ignore[typeddict-item]
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    child_scan_filters = el.find("ScanFilters")
    if child_scan_filters is not None:
        import aws_sdk_cloudformation.types.scan_filters

        out["scan_filters"] = (
            aws_sdk_cloudformation.types.scan_filters.deserialize_query(
                child_scan_filters
            )
        )
    return out
