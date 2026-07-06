"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.branch_name
    import aws_sdk_elastic_beanstalk.types.operating_system_name
    import aws_sdk_elastic_beanstalk.types.operating_system_version
    import aws_sdk_elastic_beanstalk.types.platform_arn
    import aws_sdk_elastic_beanstalk.types.platform_branch_lifecycle_state
    import aws_sdk_elastic_beanstalk.types.platform_category
    import aws_sdk_elastic_beanstalk.types.platform_lifecycle_state
    import aws_sdk_elastic_beanstalk.types.platform_owner
    import aws_sdk_elastic_beanstalk.types.platform_status
    import aws_sdk_elastic_beanstalk.types.platform_version
    import aws_sdk_elastic_beanstalk.types.supported_addon_list
    import aws_sdk_elastic_beanstalk.types.supported_tier_list


class PlatformSummary(TypedDict, closed=True):
    platform_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_arn.PlatformArn"
    ]
    """<p>The ARN of the platform version.</p>"""
    platform_owner: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_owner.PlatformOwner"
    ]
    """<p>The AWS account ID of the person who created the platform version.</p>"""
    platform_status: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_status.PlatformStatus"
    ]
    """<p>The status of the platform version. You can create an environment from the platform version once it is ready.</p>"""
    platform_category: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_category.PlatformCategory"
    ]
    """<p>The category of platform version.</p>"""
    operating_system_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.operating_system_name.OperatingSystemName"
    ]
    """<p>The operating system used by the platform version.</p>"""
    operating_system_version: NotRequired[
        "aws_sdk_elastic_beanstalk.types.operating_system_version.OperatingSystemVersion"
    ]
    """<p>The version of the operating system used by the platform version.</p>"""
    supported_tier_list: NotRequired[
        "aws_sdk_elastic_beanstalk.types.supported_tier_list.SupportedTierList"
    ]
    """<p>The tiers in which the platform version runs.</p>"""
    supported_addon_list: NotRequired[
        "aws_sdk_elastic_beanstalk.types.supported_addon_list.SupportedAddonList"
    ]
    """<p>The additions associated with the platform version.</p>"""
    platform_lifecycle_state: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_lifecycle_state.PlatformLifecycleState"
    ]
    """<p>The state of the platform version in its lifecycle.</p> <p>Possible values: <code>recommended</code> | empty</p> <p>If an empty value is returned, the platform version is supported but isn't the recommended one for its branch.</p>"""
    platform_version: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_version.PlatformVersion"
    ]
    """<p>The version string of the platform version.</p>"""
    platform_branch_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.branch_name.BranchName"
    ]
    """<p>The platform branch to which the platform version belongs.</p>"""
    platform_branch_lifecycle_state: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_branch_lifecycle_state.PlatformBranchLifecycleState"
    ]
    """<p>The state of the platform version's branch in its lifecycle.</p> <p>Possible values: <code>beta</code> | <code>supported</code> | <code>deprecated</code> | <code>retired</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_arn" in value:
        pairs.append((f"{prefix}.PlatformArn", str(value["platform_arn"])))
    if "platform_owner" in value:
        pairs.append((f"{prefix}.PlatformOwner", str(value["platform_owner"])))
    if "platform_status" in value:
        import aws_sdk_elastic_beanstalk.types.platform_status

        aws_sdk_elastic_beanstalk.types.platform_status.serialize_query(
            value["platform_status"], pairs, f"{prefix}.PlatformStatus"
        )
    if "platform_category" in value:
        pairs.append((f"{prefix}.PlatformCategory", str(value["platform_category"])))
    if "operating_system_name" in value:
        pairs.append(
            (f"{prefix}.OperatingSystemName", str(value["operating_system_name"]))
        )
    if "operating_system_version" in value:
        pairs.append(
            (f"{prefix}.OperatingSystemVersion", str(value["operating_system_version"]))
        )
    if "supported_tier_list" in value:
        import aws_sdk_elastic_beanstalk.types.supported_tier_list

        aws_sdk_elastic_beanstalk.types.supported_tier_list.serialize_query(
            value["supported_tier_list"], pairs, f"{prefix}.SupportedTierList"
        )
    if "supported_addon_list" in value:
        import aws_sdk_elastic_beanstalk.types.supported_addon_list

        aws_sdk_elastic_beanstalk.types.supported_addon_list.serialize_query(
            value["supported_addon_list"], pairs, f"{prefix}.SupportedAddonList"
        )
    if "platform_lifecycle_state" in value:
        pairs.append(
            (f"{prefix}.PlatformLifecycleState", str(value["platform_lifecycle_state"]))
        )
    if "platform_version" in value:
        pairs.append((f"{prefix}.PlatformVersion", str(value["platform_version"])))
    if "platform_branch_name" in value:
        pairs.append(
            (f"{prefix}.PlatformBranchName", str(value["platform_branch_name"]))
        )
    if "platform_branch_lifecycle_state" in value:
        pairs.append(
            (
                f"{prefix}.PlatformBranchLifecycleState",
                str(value["platform_branch_lifecycle_state"]),
            )
        )


def deserialize_query(el: Element) -> PlatformSummary:
    out: PlatformSummary = {}  # type: ignore[typeddict-item]
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_platform_owner = el.find("PlatformOwner")
    if child_platform_owner is not None:
        out["platform_owner"] = str(child_platform_owner.text or "")
    child_platform_status = el.find("PlatformStatus")
    if child_platform_status is not None:
        import aws_sdk_elastic_beanstalk.types.platform_status

        out["platform_status"] = (
            aws_sdk_elastic_beanstalk.types.platform_status.deserialize_query(
                child_platform_status
            )
        )
    child_platform_category = el.find("PlatformCategory")
    if child_platform_category is not None:
        out["platform_category"] = str(child_platform_category.text or "")
    child_operating_system_name = el.find("OperatingSystemName")
    if child_operating_system_name is not None:
        out["operating_system_name"] = str(child_operating_system_name.text or "")
    child_operating_system_version = el.find("OperatingSystemVersion")
    if child_operating_system_version is not None:
        out["operating_system_version"] = str(child_operating_system_version.text or "")
    child_supported_tier_list = el.find("SupportedTierList")
    if child_supported_tier_list is not None:
        import aws_sdk_elastic_beanstalk.types.supported_tier_list

        out["supported_tier_list"] = (
            aws_sdk_elastic_beanstalk.types.supported_tier_list.deserialize_query(
                child_supported_tier_list
            )
        )
    child_supported_addon_list = el.find("SupportedAddonList")
    if child_supported_addon_list is not None:
        import aws_sdk_elastic_beanstalk.types.supported_addon_list

        out["supported_addon_list"] = (
            aws_sdk_elastic_beanstalk.types.supported_addon_list.deserialize_query(
                child_supported_addon_list
            )
        )
    child_platform_lifecycle_state = el.find("PlatformLifecycleState")
    if child_platform_lifecycle_state is not None:
        out["platform_lifecycle_state"] = str(child_platform_lifecycle_state.text or "")
    child_platform_version = el.find("PlatformVersion")
    if child_platform_version is not None:
        out["platform_version"] = str(child_platform_version.text or "")
    child_platform_branch_name = el.find("PlatformBranchName")
    if child_platform_branch_name is not None:
        out["platform_branch_name"] = str(child_platform_branch_name.text or "")
    child_platform_branch_lifecycle_state = el.find("PlatformBranchLifecycleState")
    if child_platform_branch_lifecycle_state is not None:
        out["platform_branch_lifecycle_state"] = str(
            child_platform_branch_lifecycle_state.text or ""
        )
    return out
