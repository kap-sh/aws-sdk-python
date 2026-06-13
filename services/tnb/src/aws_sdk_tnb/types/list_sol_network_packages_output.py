"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkPackagesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_network_package_resources
    import aws_sdk_tnb.types.pagination_token


class ListSolNetworkPackagesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_tnb.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    network_packages: "aws_sdk_tnb.types.list_sol_network_package_resources.ListSolNetworkPackageResources"
    """<p>Network packages. A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkPackagesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_tnb.types.list_sol_network_package_resources

    out["networkPackages"] = (
        aws_sdk_tnb.types.list_sol_network_package_resources.serialize_json(
            value["network_packages"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListSolNetworkPackagesOutput:
    out: ListSolNetworkPackagesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "networkPackages" in data:
        import aws_sdk_tnb.types.list_sol_network_package_resources

        out["network_packages"] = (
            aws_sdk_tnb.types.list_sol_network_package_resources.deserialize_json(
                data["networkPackages"]
            )
        )
    else:
        raise DeserializationError(
            "ListSolNetworkPackagesOutput.network_packages required"
        )
    return out
