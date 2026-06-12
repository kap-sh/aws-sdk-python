"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_package_arn
    import aws_sdk_panorama.types.node_package_id
    import aws_sdk_panorama.types.node_package_name
    import aws_sdk_panorama.types.principal_arns_list
    import aws_sdk_panorama.types.storage_location
    import aws_sdk_panorama.types.tag_map
    import aws_sdk_panorama.types.time_stamp


class DescribePackageResponse(TypedDict):
    package_id: "aws_sdk_panorama.types.node_package_id.NodePackageId"
    """<p>The package's ID.</p>"""
    package_name: "aws_sdk_panorama.types.node_package_name.NodePackageName"
    """<p>The package's name.</p>"""
    arn: "aws_sdk_panorama.types.node_package_arn.NodePackageArn"
    """<p>The package's ARN.</p>"""
    storage_location: "aws_sdk_panorama.types.storage_location.StorageLocation"
    """<p>The package's storage location.</p>"""
    read_access_principal_arns: NotRequired[
        "aws_sdk_panorama.types.principal_arns_list.PrincipalArnsList"
    ]
    """<p>ARNs of accounts that have read access to the package.</p>"""
    write_access_principal_arns: NotRequired[
        "aws_sdk_panorama.types.principal_arns_list.PrincipalArnsList"
    ]
    """<p>ARNs of accounts that have write access to the package.</p>"""
    created_time: "aws_sdk_panorama.types.time_stamp.TimeStamp"
    """<p>When the package was created.</p>"""
    tags: "aws_sdk_panorama.types.tag_map.TagMap"
    """<p>The package's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageResponse) -> dict:
    out: dict = {}
    out["PackageId"] = value["package_id"]
    out["PackageName"] = value["package_name"]
    out["Arn"] = value["arn"]
    import aws_sdk_panorama.types.storage_location

    out["StorageLocation"] = aws_sdk_panorama.types.storage_location.serialize_json(
        value["storage_location"]
    )
    if "read_access_principal_arns" in value:
        import aws_sdk_panorama.types.principal_arns_list

        out["ReadAccessPrincipalArns"] = (
            aws_sdk_panorama.types.principal_arns_list.serialize_json(
                value["read_access_principal_arns"]
            )
        )
    if "write_access_principal_arns" in value:
        import aws_sdk_panorama.types.principal_arns_list

        out["WriteAccessPrincipalArns"] = (
            aws_sdk_panorama.types.principal_arns_list.serialize_json(
                value["write_access_principal_arns"]
            )
        )
    import aws_sdk_panorama.types.time_stamp

    out["CreatedTime"] = aws_sdk_panorama.types.time_stamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_panorama.types.tag_map

    out["Tags"] = aws_sdk_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribePackageResponse:
    out: DescribePackageResponse = {}  # type: ignore[typeddict-item]
    if "PackageId" in data:
        out["package_id"] = data["PackageId"]
    else:
        raise DeserializationError("DescribePackageResponse.package_id required")
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    else:
        raise DeserializationError("DescribePackageResponse.package_name required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribePackageResponse.arn required")
    if "StorageLocation" in data:
        import aws_sdk_panorama.types.storage_location

        out["storage_location"] = (
            aws_sdk_panorama.types.storage_location.deserialize_json(
                data["StorageLocation"]
            )
        )
    else:
        raise DeserializationError("DescribePackageResponse.storage_location required")
    if "ReadAccessPrincipalArns" in data:
        import aws_sdk_panorama.types.principal_arns_list

        out["read_access_principal_arns"] = (
            aws_sdk_panorama.types.principal_arns_list.deserialize_json(
                data["ReadAccessPrincipalArns"]
            )
        )
    if "WriteAccessPrincipalArns" in data:
        import aws_sdk_panorama.types.principal_arns_list

        out["write_access_principal_arns"] = (
            aws_sdk_panorama.types.principal_arns_list.deserialize_json(
                data["WriteAccessPrincipalArns"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_panorama.types.time_stamp

        out["created_time"] = aws_sdk_panorama.types.time_stamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("DescribePackageResponse.created_time required")
    if "Tags" in data:
        import aws_sdk_panorama.types.tag_map

        out["tags"] = aws_sdk_panorama.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("DescribePackageResponse.tags required")
    return out
