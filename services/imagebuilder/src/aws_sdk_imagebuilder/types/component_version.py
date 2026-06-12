"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_status
    import aws_sdk_imagebuilder.types.component_type
    import aws_sdk_imagebuilder.types.date_time
    import aws_sdk_imagebuilder.types.image_builder_arn
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.os_version_list
    import aws_sdk_imagebuilder.types.platform
    import aws_sdk_imagebuilder.types.product_code_list
    import aws_sdk_imagebuilder.types.resource_name
    import aws_sdk_imagebuilder.types.version_number


class ComponentVersion(TypedDict):
    arn: NotRequired["aws_sdk_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the component.</p> <note> <p>Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:</p> <ol> <li> <p>Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.</p> </li> <li> <p>Version ARNs have only the first three nodes: <major>.<minor>.<patch></p> </li> <li> <p>Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.</p> </li> </ol> </note>"""
    name: NotRequired["aws_sdk_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the component.</p>"""
    version: NotRequired["aws_sdk_imagebuilder.types.version_number.VersionNumber"]
    """<p>The semantic version of the component.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> <p> <b>Filtering:</b> With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the component.</p>"""
    platform: NotRequired["aws_sdk_imagebuilder.types.platform.Platform"]
    """<p>The platform of the component.</p>"""
    supported_os_versions: NotRequired[
        "aws_sdk_imagebuilder.types.os_version_list.OsVersionList"
    ]
    """<p>he operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.</p>"""
    type: NotRequired["aws_sdk_imagebuilder.types.component_type.ComponentType"]
    """<p>The type of the component denotes whether the component is used to build the image or only to test it.</p>"""
    owner: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the component.</p>"""
    date_created: NotRequired["aws_sdk_imagebuilder.types.date_time.DateTime"]
    """<p>The date that the component was created.</p>"""
    status: NotRequired["aws_sdk_imagebuilder.types.component_status.ComponentStatus"]
    """<p>Describes the current status of the component version.</p>"""
    product_codes: NotRequired[
        "aws_sdk_imagebuilder.types.product_code_list.ProductCodeList"
    ]
    """<p>Contains product codes that are used for billing purposes for Amazon Web Services Marketplace components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentVersion) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "platform" in value:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "supported_os_versions" in value:
        import aws_sdk_imagebuilder.types.os_version_list

        out["supportedOsVersions"] = (
            aws_sdk_imagebuilder.types.os_version_list.serialize_json(
                value["supported_os_versions"]
            )
        )
    if "type" in value:
        import aws_sdk_imagebuilder.types.component_type

        out["type"] = aws_sdk_imagebuilder.types.component_type.serialize_json(
            value["type"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "status" in value:
        import aws_sdk_imagebuilder.types.component_status

        out["status"] = aws_sdk_imagebuilder.types.component_status.serialize_json(
            value["status"]
        )
    if "product_codes" in value:
        import aws_sdk_imagebuilder.types.product_code_list

        out["productCodes"] = (
            aws_sdk_imagebuilder.types.product_code_list.serialize_json(
                value["product_codes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentVersion:
    out: ComponentVersion = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "description" in data:
        out["description"] = data["description"]
    if "platform" in data:
        import aws_sdk_imagebuilder.types.platform

        out["platform"] = aws_sdk_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if "supportedOsVersions" in data:
        import aws_sdk_imagebuilder.types.os_version_list

        out["supported_os_versions"] = (
            aws_sdk_imagebuilder.types.os_version_list.deserialize_json(
                data["supportedOsVersions"]
            )
        )
    if "type" in data:
        import aws_sdk_imagebuilder.types.component_type

        out["type"] = aws_sdk_imagebuilder.types.component_type.deserialize_json(
            data["type"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "status" in data:
        import aws_sdk_imagebuilder.types.component_status

        out["status"] = aws_sdk_imagebuilder.types.component_status.deserialize_json(
            data["status"]
        )
    if "productCodes" in data:
        import aws_sdk_imagebuilder.types.product_code_list

        out["product_codes"] = (
            aws_sdk_imagebuilder.types.product_code_list.deserialize_json(
                data["productCodes"]
            )
        )
    return out
