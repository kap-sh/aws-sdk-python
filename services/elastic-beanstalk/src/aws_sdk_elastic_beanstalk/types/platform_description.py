"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.branch_name
    import aws_sdk_elastic_beanstalk.types.creation_date
    import aws_sdk_elastic_beanstalk.types.custom_ami_list
    import aws_sdk_elastic_beanstalk.types.description
    import aws_sdk_elastic_beanstalk.types.maintainer
    import aws_sdk_elastic_beanstalk.types.operating_system_name
    import aws_sdk_elastic_beanstalk.types.operating_system_version
    import aws_sdk_elastic_beanstalk.types.platform_arn
    import aws_sdk_elastic_beanstalk.types.platform_branch_lifecycle_state
    import aws_sdk_elastic_beanstalk.types.platform_category
    import aws_sdk_elastic_beanstalk.types.platform_frameworks
    import aws_sdk_elastic_beanstalk.types.platform_lifecycle_state
    import aws_sdk_elastic_beanstalk.types.platform_name
    import aws_sdk_elastic_beanstalk.types.platform_owner
    import aws_sdk_elastic_beanstalk.types.platform_programming_languages
    import aws_sdk_elastic_beanstalk.types.platform_status
    import aws_sdk_elastic_beanstalk.types.platform_version
    import aws_sdk_elastic_beanstalk.types.solution_stack_name
    import aws_sdk_elastic_beanstalk.types.supported_addon_list
    import aws_sdk_elastic_beanstalk.types.supported_tier_list
    import aws_sdk_elastic_beanstalk.types.update_date


class PlatformDescription(TypedDict):
    platform_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_arn.PlatformArn"
    ]
    """<p>The ARN of the platform version.</p>"""
    platform_owner: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_owner.PlatformOwner"
    ]
    """<p>The AWS account ID of the person who created the platform version.</p>"""
    platform_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_name.PlatformName"
    ]
    """<p>The name of the platform version.</p>"""
    platform_version: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_version.PlatformVersion"
    ]
    """<p>The version of the platform version.</p>"""
    solution_stack_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>The name of the solution stack used by the platform version.</p>"""
    platform_status: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_status.PlatformStatus"
    ]
    """<p>The status of the platform version.</p>"""
    date_created: NotRequired[
        "aws_sdk_elastic_beanstalk.types.creation_date.CreationDate"
    ]
    """<p>The date when the platform version was created.</p>"""
    date_updated: NotRequired["aws_sdk_elastic_beanstalk.types.update_date.UpdateDate"]
    """<p>The date when the platform version was last updated.</p>"""
    platform_category: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_category.PlatformCategory"
    ]
    """<p>The category of the platform version.</p>"""
    description: NotRequired["aws_sdk_elastic_beanstalk.types.description.Description"]
    """<p>The description of the platform version.</p>"""
    maintainer: NotRequired["aws_sdk_elastic_beanstalk.types.maintainer.Maintainer"]
    """<p>Information about the maintainer of the platform version.</p>"""
    operating_system_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.operating_system_name.OperatingSystemName"
    ]
    """<p>The operating system used by the platform version.</p>"""
    operating_system_version: NotRequired[
        "aws_sdk_elastic_beanstalk.types.operating_system_version.OperatingSystemVersion"
    ]
    """<p>The version of the operating system used by the platform version.</p>"""
    programming_languages: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_programming_languages.PlatformProgrammingLanguages"
    ]
    """<p>The programming languages supported by the platform version.</p>"""
    frameworks: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_frameworks.PlatformFrameworks"
    ]
    """<p>The frameworks supported by the platform version.</p>"""
    custom_ami_list: NotRequired[
        "aws_sdk_elastic_beanstalk.types.custom_ami_list.CustomAmiList"
    ]
    """<p>The custom AMIs supported by the platform version.</p>"""
    supported_tier_list: NotRequired[
        "aws_sdk_elastic_beanstalk.types.supported_tier_list.SupportedTierList"
    ]
    """<p>The tiers supported by the platform version.</p>"""
    supported_addon_list: NotRequired[
        "aws_sdk_elastic_beanstalk.types.supported_addon_list.SupportedAddonList"
    ]
    """<p>The additions supported by the platform version.</p>"""
    platform_lifecycle_state: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_lifecycle_state.PlatformLifecycleState"
    ]
    """<p>The state of the platform version in its lifecycle.</p> <p>Possible values: <code>Recommended</code> | <code>null</code> </p> <p>If a null value is returned, the platform version isn't the recommended one for its branch. Each platform branch has a single recommended platform version, typically the most recent one.</p>"""
    platform_branch_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.branch_name.BranchName"
    ]
    """<p>The platform branch to which the platform version belongs.</p>"""
    platform_branch_lifecycle_state: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_branch_lifecycle_state.PlatformBranchLifecycleState"
    ]
    """<p>The state of the platform version's branch in its lifecycle.</p> <p>Possible values: <code>Beta</code> | <code>Supported</code> | <code>Deprecated</code> | <code>Retired</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "platform_arn" in value:
        pairs.append((f"{prefix}.PlatformArn", str(value["platform_arn"])))
    if "platform_owner" in value:
        pairs.append((f"{prefix}.PlatformOwner", str(value["platform_owner"])))
    if "platform_name" in value:
        pairs.append((f"{prefix}.PlatformName", str(value["platform_name"])))
    if "platform_version" in value:
        pairs.append((f"{prefix}.PlatformVersion", str(value["platform_version"])))
    if "solution_stack_name" in value:
        pairs.append((f"{prefix}.SolutionStackName", str(value["solution_stack_name"])))
    if "platform_status" in value:
        import aws_sdk_elastic_beanstalk.types.platform_status

        aws_sdk_elastic_beanstalk.types.platform_status.serialize_query(
            value["platform_status"], pairs, f"{prefix}.PlatformStatus"
        )
    if "date_created" in value:
        import aws_sdk_elastic_beanstalk.types.creation_date

        aws_sdk_elastic_beanstalk.types.creation_date.serialize_query(
            value["date_created"], pairs, f"{prefix}.DateCreated"
        )
    if "date_updated" in value:
        import aws_sdk_elastic_beanstalk.types.update_date

        aws_sdk_elastic_beanstalk.types.update_date.serialize_query(
            value["date_updated"], pairs, f"{prefix}.DateUpdated"
        )
    if "platform_category" in value:
        pairs.append((f"{prefix}.PlatformCategory", str(value["platform_category"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "maintainer" in value:
        pairs.append((f"{prefix}.Maintainer", str(value["maintainer"])))
    if "operating_system_name" in value:
        pairs.append(
            (f"{prefix}.OperatingSystemName", str(value["operating_system_name"]))
        )
    if "operating_system_version" in value:
        pairs.append(
            (f"{prefix}.OperatingSystemVersion", str(value["operating_system_version"]))
        )
    if "programming_languages" in value:
        import aws_sdk_elastic_beanstalk.types.platform_programming_languages

        aws_sdk_elastic_beanstalk.types.platform_programming_languages.serialize_query(
            value["programming_languages"], pairs, f"{prefix}.ProgrammingLanguages"
        )
    if "frameworks" in value:
        import aws_sdk_elastic_beanstalk.types.platform_frameworks

        aws_sdk_elastic_beanstalk.types.platform_frameworks.serialize_query(
            value["frameworks"], pairs, f"{prefix}.Frameworks"
        )
    if "custom_ami_list" in value:
        import aws_sdk_elastic_beanstalk.types.custom_ami_list

        aws_sdk_elastic_beanstalk.types.custom_ami_list.serialize_query(
            value["custom_ami_list"], pairs, f"{prefix}.CustomAmiList"
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


def deserialize_query(el: Element) -> PlatformDescription:
    out: PlatformDescription = {}  # type: ignore[typeddict-item]
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_platform_owner = el.find("PlatformOwner")
    if child_platform_owner is not None:
        out["platform_owner"] = str(child_platform_owner.text or "")
    child_platform_name = el.find("PlatformName")
    if child_platform_name is not None:
        out["platform_name"] = str(child_platform_name.text or "")
    child_platform_version = el.find("PlatformVersion")
    if child_platform_version is not None:
        out["platform_version"] = str(child_platform_version.text or "")
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_status = el.find("PlatformStatus")
    if child_platform_status is not None:
        import aws_sdk_elastic_beanstalk.types.platform_status

        out["platform_status"] = (
            aws_sdk_elastic_beanstalk.types.platform_status.deserialize_query(
                child_platform_status
            )
        )
    child_date_created = el.find("DateCreated")
    if child_date_created is not None:
        import aws_sdk_elastic_beanstalk.types.creation_date

        out["date_created"] = (
            aws_sdk_elastic_beanstalk.types.creation_date.deserialize_query(
                child_date_created
            )
        )
    child_date_updated = el.find("DateUpdated")
    if child_date_updated is not None:
        import aws_sdk_elastic_beanstalk.types.update_date

        out["date_updated"] = (
            aws_sdk_elastic_beanstalk.types.update_date.deserialize_query(
                child_date_updated
            )
        )
    child_platform_category = el.find("PlatformCategory")
    if child_platform_category is not None:
        out["platform_category"] = str(child_platform_category.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_maintainer = el.find("Maintainer")
    if child_maintainer is not None:
        out["maintainer"] = str(child_maintainer.text or "")
    child_operating_system_name = el.find("OperatingSystemName")
    if child_operating_system_name is not None:
        out["operating_system_name"] = str(child_operating_system_name.text or "")
    child_operating_system_version = el.find("OperatingSystemVersion")
    if child_operating_system_version is not None:
        out["operating_system_version"] = str(child_operating_system_version.text or "")
    child_programming_languages = el.find("ProgrammingLanguages")
    if child_programming_languages is not None:
        import aws_sdk_elastic_beanstalk.types.platform_programming_languages

        out["programming_languages"] = (
            aws_sdk_elastic_beanstalk.types.platform_programming_languages.deserialize_query(
                child_programming_languages
            )
        )
    child_frameworks = el.find("Frameworks")
    if child_frameworks is not None:
        import aws_sdk_elastic_beanstalk.types.platform_frameworks

        out["frameworks"] = (
            aws_sdk_elastic_beanstalk.types.platform_frameworks.deserialize_query(
                child_frameworks
            )
        )
    child_custom_ami_list = el.find("CustomAmiList")
    if child_custom_ami_list is not None:
        import aws_sdk_elastic_beanstalk.types.custom_ami_list

        out["custom_ami_list"] = (
            aws_sdk_elastic_beanstalk.types.custom_ami_list.deserialize_query(
                child_custom_ami_list
            )
        )
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
    child_platform_branch_name = el.find("PlatformBranchName")
    if child_platform_branch_name is not None:
        out["platform_branch_name"] = str(child_platform_branch_name.text or "")
    child_platform_branch_lifecycle_state = el.find("PlatformBranchLifecycleState")
    if child_platform_branch_lifecycle_state is not None:
        out["platform_branch_lifecycle_state"] = str(
            child_platform_branch_lifecycle_state.text or ""
        )
    return out
