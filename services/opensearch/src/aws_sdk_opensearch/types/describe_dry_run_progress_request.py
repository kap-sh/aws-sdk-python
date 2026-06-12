"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDryRunProgressRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.guid


class DescribeDryRunProgressRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    dry_run_id: NotRequired["aws_sdk_opensearch.types.guid.GUID"]
    """<p>The unique identifier of the dry run.</p>"""
    load_dry_run_config: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether to include the configuration of the dry run in the response. The configuration specifies the updates that you're planning to make on the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDryRunProgressRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDryRunProgressRequest:
    out: DescribeDryRunProgressRequest = {}  # type: ignore[typeddict-item]
    return out
