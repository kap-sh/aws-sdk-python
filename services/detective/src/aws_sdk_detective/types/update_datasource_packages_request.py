"""Generated from Smithy shape ``com.amazonaws.detective#UpdateDatasourcePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.datasource_package_list
    import aws_sdk_detective.types.graph_arn


class UpdateDatasourcePackagesRequest(TypedDict, closed=True):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    datasource_packages: (
        "aws_sdk_detective.types.datasource_package_list.DatasourcePackageList"
    )
    """<p>The data source package to start for the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasourcePackagesRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    import aws_sdk_detective.types.datasource_package_list

    out["DatasourcePackages"] = (
        aws_sdk_detective.types.datasource_package_list.serialize_json(
            value["datasource_packages"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDatasourcePackagesRequest:
    out: UpdateDatasourcePackagesRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("UpdateDatasourcePackagesRequest.graph_arn required")
    if "DatasourcePackages" in data:
        import aws_sdk_detective.types.datasource_package_list

        out["datasource_packages"] = (
            aws_sdk_detective.types.datasource_package_list.deserialize_json(
                data["DatasourcePackages"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDatasourcePackagesRequest.datasource_packages required"
        )
    return out
