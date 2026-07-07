"""Generated from Smithy shape ``com.amazonaws.servicecatalog#LaunchPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.portfolio_name


class LaunchPath(TypedDict, closed=True):
    id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the launch path.</p>"""
    name: NotRequired["aws_sdk_service_catalog.types.portfolio_name.PortfolioName"]
    """<p>The name of the launch path.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LaunchPath) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LaunchPath:
    out: LaunchPath = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
