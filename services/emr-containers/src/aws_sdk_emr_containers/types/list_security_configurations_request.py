"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListSecurityConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.java_integer
    import aws_sdk_emr_containers.types.next_token


class ListSecurityConfigurationsRequest(TypedDict):
    created_after: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time after which the security configuration was created.</p>"""
    created_before: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time before which the security configuration was created.</p>"""
    max_results: NotRequired["aws_sdk_emr_containers.types.java_integer.JavaInteger"]
    """<p>The maximum number of security configurations the operation can list.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p>The token for the next set of security configurations to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSecurityConfigurationsRequest:
    out: ListSecurityConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
