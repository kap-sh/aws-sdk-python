"""Generated from Smithy shape ``com.amazonaws.route53domains#GetDomainSuggestionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_suggestions_list


class GetDomainSuggestionsResponse(TypedDict):
    suggestions_list: NotRequired[
        "aws_sdk_route_53_domains.types.domain_suggestions_list.DomainSuggestionsList"
    ]
    """<p>A list of possible domain names. If you specified <code>true</code> for <code>OnlyAvailable</code> in the request, the list contains only domains that are available for registration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainSuggestionsResponse) -> dict:
    out: dict = {}
    if "suggestions_list" in value:
        import aws_sdk_route_53_domains.types.domain_suggestions_list

        out["SuggestionsList"] = (
            aws_sdk_route_53_domains.types.domain_suggestions_list.serialize_aws_json_1_1(
                value["suggestions_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainSuggestionsResponse:
    out: GetDomainSuggestionsResponse = {}  # type: ignore[typeddict-item]
    if "SuggestionsList" in data:
        import aws_sdk_route_53_domains.types.domain_suggestions_list

        out["suggestions_list"] = (
            aws_sdk_route_53_domains.types.domain_suggestions_list.deserialize_aws_json_1_1(
                data["SuggestionsList"]
            )
        )
    return out
