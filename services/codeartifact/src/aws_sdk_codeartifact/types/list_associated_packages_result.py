"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListAssociatedPackagesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.associated_package_list
    import aws_sdk_codeartifact.types.pagination_token


class ListAssociatedPackagesResult(TypedDict):
    packages: NotRequired[
        "aws_sdk_codeartifact.types.associated_package_list.AssociatedPackageList"
    ]
    """<p> The list of packages associated with the requested package group. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedPackagesResult) -> dict:
    out: dict = {}
    if "packages" in value:
        import aws_sdk_codeartifact.types.associated_package_list

        out["packages"] = (
            aws_sdk_codeartifact.types.associated_package_list.serialize_json(
                value["packages"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedPackagesResult:
    out: ListAssociatedPackagesResult = {}  # type: ignore[typeddict-item]
    if "packages" in data:
        import aws_sdk_codeartifact.types.associated_package_list

        out["packages"] = (
            aws_sdk_codeartifact.types.associated_package_list.deserialize_json(
                data["packages"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
