"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCodeSecurityScanConfigurationAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_scan_configuration_association_summaries
    import aws_sdk_inspector2.types.next_token


class ListCodeSecurityScanConfigurationAssociationsResponse(TypedDict):
    associations: NotRequired[
        "aws_sdk_inspector2.types.code_security_scan_configuration_association_summaries.CodeSecurityScanConfigurationAssociationSummaries"
    ]
    """<p>A list of associations between code repositories and scan configurations.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ListCodeSecurityScanConfigurationAssociationsResponse,
) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_inspector2.types.code_security_scan_configuration_association_summaries

        out["associations"] = (
            aws_sdk_inspector2.types.code_security_scan_configuration_association_summaries.serialize_json(
                value["associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> ListCodeSecurityScanConfigurationAssociationsResponse:
    out: ListCodeSecurityScanConfigurationAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "associations" in data:
        import aws_sdk_inspector2.types.code_security_scan_configuration_association_summaries

        out["associations"] = (
            aws_sdk_inspector2.types.code_security_scan_configuration_association_summaries.deserialize_json(
                data["associations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
