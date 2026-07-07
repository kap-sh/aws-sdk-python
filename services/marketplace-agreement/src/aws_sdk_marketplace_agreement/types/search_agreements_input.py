"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SearchAgreementsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.catalog
    import aws_sdk_marketplace_agreement.types.filter_list
    import aws_sdk_marketplace_agreement.types.max_results
    import aws_sdk_marketplace_agreement.types.next_token
    import aws_sdk_marketplace_agreement.types.sort


class SearchAgreementsInput(TypedDict, closed=True):
    catalog: NotRequired["aws_sdk_marketplace_agreement.types.catalog.Catalog"]
    """<p>The catalog in which the agreement was created.</p>"""
    filters: NotRequired["aws_sdk_marketplace_agreement.types.filter_list.FilterList"]
    """<p>The filter name and value pair used to return a specific list of results.</p> <p>The following filters are supported:</p> <ul> <li> <p> <code>ResourceIdentifier</code> – The unique identifier of the resource.</p> </li> <li> <p> <code>ResourceType</code> – Type of the resource, which is the product (<code>AmiProduct</code>, <code>ContainerProduct</code>, <code>SaaSProduct</code>, <code>ProfessionalServicesProduct</code>, or <code>MachineLearningProduct</code>).</p> </li> <li> <p> <code>PartyType</code> – The party type of the caller. Use <code>Proposer</code> or <code>Acceptor</code>.</p> </li> <li> <p> <code>AcceptorAccountId</code> – The AWS account ID of the party accepting the agreement terms.</p> </li> <li> <p> <code>OfferId</code> – The unique identifier of the offer in which the terms are registered in the agreement token.</p> </li> <li> <p> <code>Status</code> – The current status of the agreement. Values include <code>ACTIVE</code>, <code>ARCHIVED</code>, <code>CANCELLED</code>, <code>EXPIRED</code>, <code>RENEWED</code>, <code>REPLACED</code>, and <code>TERMINATED</code>.</p> </li> <li> <p> <code>BeforeEndTime</code> – A date used to filter agreements with a date before the <code>endTime</code> of an agreement.</p> </li> <li> <p> <code>AfterEndTime</code> – A date used to filter agreements with a date after the <code>endTime</code> of an agreement.</p> </li> <li> <p> <code>AgreementType</code> – The type of agreement. Supported value includes <code>PurchaseAgreement</code>.</p> </li> <li> <p> <code>OfferSetId</code> – A unique identifier for the offer set containing this offer. All agreements created from offers in this set include this identifier as context.</p> </li> </ul>"""
    sort: NotRequired["aws_sdk_marketplace_agreement.types.sort.Sort"]
    """<p>An object that contains the <code>SortBy</code> and <code>SortOrder</code> attributes. Only <code>EndTime</code> is supported for <code>SearchAgreements</code>. The default sort is <code>EndTime</code> descending.</p>"""
    max_results: NotRequired[
        "aws_sdk_marketplace_agreement.types.max_results.MaxResults"
    ]
    """<p>The maximum number of agreements to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchAgreementsInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "filters" in value:
        import aws_sdk_marketplace_agreement.types.filter_list

        out["filters"] = (
            aws_sdk_marketplace_agreement.types.filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "sort" in value:
        import aws_sdk_marketplace_agreement.types.sort

        out["sort"] = aws_sdk_marketplace_agreement.types.sort.serialize_aws_json_1_0(
            value["sort"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchAgreementsInput:
    out: SearchAgreementsInput = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    if "filters" in data:
        import aws_sdk_marketplace_agreement.types.filter_list

        out["filters"] = (
            aws_sdk_marketplace_agreement.types.filter_list.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "sort" in data:
        import aws_sdk_marketplace_agreement.types.sort

        out["sort"] = aws_sdk_marketplace_agreement.types.sort.deserialize_aws_json_1_0(
            data["sort"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
