"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainSuggestionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_suggestion

DomainSuggestionsList: TypeAlias = list[
    "aws_sdk_route_53_domains.types.domain_suggestion.DomainSuggestion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainSuggestionsList) -> list:
    import aws_sdk_route_53_domains.types.domain_suggestion

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route_53_domains.types.domain_suggestion.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DomainSuggestionsList:
    import aws_sdk_route_53_domains.types.domain_suggestion

    out: DomainSuggestionsList = []
    for item in data:
        out.append(
            aws_sdk_route_53_domains.types.domain_suggestion.deserialize_aws_json_1_1(
                item
            )
        )
    return out
