"""Generated from Smithy shape ``com.amazonaws.appsync#ListDomainNamesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.domain_name_configs
    import aws_sdk_appsync.types.pagination_token


class ListDomainNamesResponse(TypedDict, closed=True):
    domain_name_configs: NotRequired[
        "aws_sdk_appsync.types.domain_name_configs.DomainNameConfigs"
    ]
    """<p>Lists configurations for multiple domain names.</p>"""
    next_token: NotRequired["aws_sdk_appsync.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainNamesResponse) -> dict:
    out: dict = {}
    if "domain_name_configs" in value:
        import aws_sdk_appsync.types.domain_name_configs

        out["domainNameConfigs"] = (
            aws_sdk_appsync.types.domain_name_configs.serialize_json(
                value["domain_name_configs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainNamesResponse:
    out: ListDomainNamesResponse = {}  # type: ignore[typeddict-item]
    if "domainNameConfigs" in data:
        import aws_sdk_appsync.types.domain_name_configs

        out["domain_name_configs"] = (
            aws_sdk_appsync.types.domain_name_configs.deserialize_json(
                data["domainNameConfigs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
