"""Generated from Smithy shape ``com.amazonaws.opensearch#AssociatePackagesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_package_details_list


class AssociatePackagesResponse(TypedDict):
    domain_package_details_list: NotRequired[
        "aws_sdk_opensearch.types.domain_package_details_list.DomainPackageDetailsList"
    ]
    """<p>List of information about packages that are associated with a domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePackagesResponse) -> dict:
    out: dict = {}
    if "domain_package_details_list" in value:
        import aws_sdk_opensearch.types.domain_package_details_list

        out["DomainPackageDetailsList"] = (
            aws_sdk_opensearch.types.domain_package_details_list.serialize_json(
                value["domain_package_details_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociatePackagesResponse:
    out: AssociatePackagesResponse = {}  # type: ignore[typeddict-item]
    if "DomainPackageDetailsList" in data:
        import aws_sdk_opensearch.types.domain_package_details_list

        out["domain_package_details_list"] = (
            aws_sdk_opensearch.types.domain_package_details_list.deserialize_json(
                data["DomainPackageDetailsList"]
            )
        )
    return out
