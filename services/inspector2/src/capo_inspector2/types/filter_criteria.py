"""Generated from Smithy shape ``com.amazonaws.inspector2#FilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_filter_list
    import capo_inspector2.types.map_filter_list
    import capo_inspector2.types.number_filter_list
    import capo_inspector2.types.package_filter_list
    import capo_inspector2.types.port_range_filter_list
    import capo_inspector2.types.string_filter_list


class FilterCriteria(TypedDict, closed=True):
    finding_arn: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the finding ARNs used to filter findings.</p>"""
    aws_account_id: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon Web Services account IDs used to filter findings.</p>"""
    finding_type: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the finding types used to filter findings.</p>"""
    severity: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>Details on the severity used to filter findings.</p>"""
    first_observed_at: NotRequired[
        "capo_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Details on the date and time a finding was first seen used to filter findings.</p>"""
    last_observed_at: NotRequired[
        "capo_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Details on the date and time a finding was last seen used to filter findings.</p>"""
    updated_at: NotRequired["capo_inspector2.types.date_filter_list.DateFilterList"]
    """<p>Details on the date and time a finding was last updated at used to filter findings.</p>"""
    finding_status: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the finding status types used to filter findings.</p>"""
    title: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>Details on the finding title used to filter findings.</p>"""
    inspector_score: NotRequired[
        "capo_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>The Amazon Inspector score to filter on.</p>"""
    resource_type: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the resource types used to filter findings.</p>"""
    resource_id: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the resource IDs used to filter findings.</p>"""
    resource_tags: NotRequired["capo_inspector2.types.map_filter_list.MapFilterList"]
    """<p>Details on the resource tags used to filter findings.</p>"""
    ec2_instance_image_id: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon EC2 instance image IDs used to filter findings.</p>"""
    ec2_instance_vpc_id: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon EC2 instance VPC IDs used to filter findings.</p>"""
    ec2_instance_subnet_id: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon EC2 instance subnet IDs used to filter findings.</p>"""
    ecr_image_pushed_at: NotRequired[
        "capo_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Details on the Amazon ECR image push date and time used to filter findings.</p>"""
    ecr_image_architecture: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon ECR image architecture types used to filter findings.</p>"""
    ecr_image_registry: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the Amazon ECR registry used to filter findings.</p>"""
    ecr_image_repository_name: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the name of the Amazon ECR repository used to filter findings.</p>"""
    ecr_image_tags: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The tags attached to the Amazon ECR container image.</p>"""
    ecr_image_hash: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon ECR image hashes used to filter findings.</p>"""
    ecr_image_last_in_use_at: NotRequired[
        "capo_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Filter criteria indicating when an Amazon ECR image was last used in an Amazon ECS cluster task or Amazon EKS cluster pod.</p>"""
    ecr_image_in_use_count: NotRequired[
        "capo_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>Filter criteria indicating when details for an Amazon ECR image include when an Amazon ECR image is in use.</p>"""
    port_range: NotRequired[
        "capo_inspector2.types.port_range_filter_list.PortRangeFilterList"
    ]
    """<p>Details on the port ranges used to filter findings.</p>"""
    network_protocol: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on network protocol used to filter findings.</p>"""
    component_id: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the component IDs used to filter findings.</p>"""
    component_type: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the component types used to filter findings.</p>"""
    vulnerability_id: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the vulnerability ID used to filter findings.</p>"""
    vulnerability_source: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the vulnerability type used to filter findings.</p>"""
    vendor_severity: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the vendor severity used to filter findings.</p>"""
    vulnerable_packages: NotRequired[
        "capo_inspector2.types.package_filter_list.PackageFilterList"
    ]
    """<p>Details on the vulnerable packages used to filter findings.</p>"""
    related_vulnerabilities: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the related vulnerabilities used to filter findings.</p>"""
    fix_available: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on whether a fix is available through a version update. This value can be <code>YES</code>, <code>NO</code>, or <code>PARTIAL</code>. A <code>PARTIAL</code> fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.</p>"""
    lambda_function_name: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by the name of the function.</p>"""
    lambda_function_layers: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    r"""<p>Filters the list of Amazon Web Services Lambda functions by the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\"> layers</a>. A Lambda function can have up to five layers.</p>"""
    lambda_function_runtime: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by the runtime environment for the Lambda function.</p>"""
    lambda_function_last_modified_at: NotRequired[
        "capo_inspector2.types.date_filter_list.DateFilterList"
    ]
    r"""<p>Filters the list of Amazon Web Services Lambda functions by the date and time that a user last updated the configuration, in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601 format</a> </p>"""
    lambda_function_execution_role_arn: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by execution role.</p>"""
    exploit_available: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda findings by the availability of exploits.</p>"""
    code_vulnerability_detector_name: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The name of the detector used to identify a code vulnerability in a Lambda function used to filter findings.</p>"""
    code_vulnerability_detector_tags: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    r"""<p>The detector type tag associated with the vulnerability used to filter findings. Detector tags group related vulnerabilities by common themes or tactics. For a list of available tags by programming language, see <a href=\"https://docs.aws.amazon.com/codeguru/detector-library/java/tags/\">Java tags</a>, or <a href=\"https://docs.aws.amazon.com/codeguru/detector-library/python/tags/\">Python tags</a>. </p>"""
    code_vulnerability_file_path: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The file path to the file in a Lambda function that contains a code vulnerability used to filter findings.</p>"""
    epss_score: NotRequired["capo_inspector2.types.number_filter_list.NumberFilterList"]
    """<p>The EPSS score used to filter findings.</p>"""
    code_repository_project_name: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filter criteria for findings based on the project name in a code repository.</p>"""
    code_repository_provider_type: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filter criteria for findings based on the repository provider type (such as GitHub, GitLab, etc.).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "finding_arn" in value:
        import capo_inspector2.types.string_filter_list

        out["findingArn"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["finding_arn"]
        )
    if "aws_account_id" in value:
        import capo_inspector2.types.string_filter_list

        out["awsAccountId"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["aws_account_id"]
        )
    if "finding_type" in value:
        import capo_inspector2.types.string_filter_list

        out["findingType"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["finding_type"]
        )
    if "severity" in value:
        import capo_inspector2.types.string_filter_list

        out["severity"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["severity"]
        )
    if "first_observed_at" in value:
        import capo_inspector2.types.date_filter_list

        out["firstObservedAt"] = capo_inspector2.types.date_filter_list.serialize_json(
            value["first_observed_at"]
        )
    if "last_observed_at" in value:
        import capo_inspector2.types.date_filter_list

        out["lastObservedAt"] = capo_inspector2.types.date_filter_list.serialize_json(
            value["last_observed_at"]
        )
    if "updated_at" in value:
        import capo_inspector2.types.date_filter_list

        out["updatedAt"] = capo_inspector2.types.date_filter_list.serialize_json(
            value["updated_at"]
        )
    if "finding_status" in value:
        import capo_inspector2.types.string_filter_list

        out["findingStatus"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["finding_status"]
        )
    if "title" in value:
        import capo_inspector2.types.string_filter_list

        out["title"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["title"]
        )
    if "inspector_score" in value:
        import capo_inspector2.types.number_filter_list

        out["inspectorScore"] = capo_inspector2.types.number_filter_list.serialize_json(
            value["inspector_score"]
        )
    if "resource_type" in value:
        import capo_inspector2.types.string_filter_list

        out["resourceType"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["resource_type"]
        )
    if "resource_id" in value:
        import capo_inspector2.types.string_filter_list

        out["resourceId"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["resource_id"]
        )
    if "resource_tags" in value:
        import capo_inspector2.types.map_filter_list

        out["resourceTags"] = capo_inspector2.types.map_filter_list.serialize_json(
            value["resource_tags"]
        )
    if "ec2_instance_image_id" in value:
        import capo_inspector2.types.string_filter_list

        out["ec2InstanceImageId"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["ec2_instance_image_id"]
            )
        )
    if "ec2_instance_vpc_id" in value:
        import capo_inspector2.types.string_filter_list

        out["ec2InstanceVpcId"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["ec2_instance_vpc_id"]
            )
        )
    if "ec2_instance_subnet_id" in value:
        import capo_inspector2.types.string_filter_list

        out["ec2InstanceSubnetId"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["ec2_instance_subnet_id"]
            )
        )
    if "ecr_image_pushed_at" in value:
        import capo_inspector2.types.date_filter_list

        out["ecrImagePushedAt"] = capo_inspector2.types.date_filter_list.serialize_json(
            value["ecr_image_pushed_at"]
        )
    if "ecr_image_architecture" in value:
        import capo_inspector2.types.string_filter_list

        out["ecrImageArchitecture"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_architecture"]
            )
        )
    if "ecr_image_registry" in value:
        import capo_inspector2.types.string_filter_list

        out["ecrImageRegistry"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_registry"]
            )
        )
    if "ecr_image_repository_name" in value:
        import capo_inspector2.types.string_filter_list

        out["ecrImageRepositoryName"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_repository_name"]
            )
        )
    if "ecr_image_tags" in value:
        import capo_inspector2.types.string_filter_list

        out["ecrImageTags"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["ecr_image_tags"]
        )
    if "ecr_image_hash" in value:
        import capo_inspector2.types.string_filter_list

        out["ecrImageHash"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["ecr_image_hash"]
        )
    if "ecr_image_last_in_use_at" in value:
        import capo_inspector2.types.date_filter_list

        out["ecrImageLastInUseAt"] = (
            capo_inspector2.types.date_filter_list.serialize_json(
                value["ecr_image_last_in_use_at"]
            )
        )
    if "ecr_image_in_use_count" in value:
        import capo_inspector2.types.number_filter_list

        out["ecrImageInUseCount"] = (
            capo_inspector2.types.number_filter_list.serialize_json(
                value["ecr_image_in_use_count"]
            )
        )
    if "port_range" in value:
        import capo_inspector2.types.port_range_filter_list

        out["portRange"] = capo_inspector2.types.port_range_filter_list.serialize_json(
            value["port_range"]
        )
    if "network_protocol" in value:
        import capo_inspector2.types.string_filter_list

        out["networkProtocol"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["network_protocol"]
            )
        )
    if "component_id" in value:
        import capo_inspector2.types.string_filter_list

        out["componentId"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["component_id"]
        )
    if "component_type" in value:
        import capo_inspector2.types.string_filter_list

        out["componentType"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["component_type"]
        )
    if "vulnerability_id" in value:
        import capo_inspector2.types.string_filter_list

        out["vulnerabilityId"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["vulnerability_id"]
            )
        )
    if "vulnerability_source" in value:
        import capo_inspector2.types.string_filter_list

        out["vulnerabilitySource"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["vulnerability_source"]
            )
        )
    if "vendor_severity" in value:
        import capo_inspector2.types.string_filter_list

        out["vendorSeverity"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["vendor_severity"]
        )
    if "vulnerable_packages" in value:
        import capo_inspector2.types.package_filter_list

        out["vulnerablePackages"] = (
            capo_inspector2.types.package_filter_list.serialize_json(
                value["vulnerable_packages"]
            )
        )
    if "related_vulnerabilities" in value:
        import capo_inspector2.types.string_filter_list

        out["relatedVulnerabilities"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["related_vulnerabilities"]
            )
        )
    if "fix_available" in value:
        import capo_inspector2.types.string_filter_list

        out["fixAvailable"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["fix_available"]
        )
    if "lambda_function_name" in value:
        import capo_inspector2.types.string_filter_list

        out["lambdaFunctionName"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_name"]
            )
        )
    if "lambda_function_layers" in value:
        import capo_inspector2.types.string_filter_list

        out["lambdaFunctionLayers"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_layers"]
            )
        )
    if "lambda_function_runtime" in value:
        import capo_inspector2.types.string_filter_list

        out["lambdaFunctionRuntime"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_runtime"]
            )
        )
    if "lambda_function_last_modified_at" in value:
        import capo_inspector2.types.date_filter_list

        out["lambdaFunctionLastModifiedAt"] = (
            capo_inspector2.types.date_filter_list.serialize_json(
                value["lambda_function_last_modified_at"]
            )
        )
    if "lambda_function_execution_role_arn" in value:
        import capo_inspector2.types.string_filter_list

        out["lambdaFunctionExecutionRoleArn"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_execution_role_arn"]
            )
        )
    if "exploit_available" in value:
        import capo_inspector2.types.string_filter_list

        out["exploitAvailable"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["exploit_available"]
            )
        )
    if "code_vulnerability_detector_name" in value:
        import capo_inspector2.types.string_filter_list

        out["codeVulnerabilityDetectorName"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["code_vulnerability_detector_name"]
            )
        )
    if "code_vulnerability_detector_tags" in value:
        import capo_inspector2.types.string_filter_list

        out["codeVulnerabilityDetectorTags"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["code_vulnerability_detector_tags"]
            )
        )
    if "code_vulnerability_file_path" in value:
        import capo_inspector2.types.string_filter_list

        out["codeVulnerabilityFilePath"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["code_vulnerability_file_path"]
            )
        )
    if "epss_score" in value:
        import capo_inspector2.types.number_filter_list

        out["epssScore"] = capo_inspector2.types.number_filter_list.serialize_json(
            value["epss_score"]
        )
    if "code_repository_project_name" in value:
        import capo_inspector2.types.string_filter_list

        out["codeRepositoryProjectName"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["code_repository_project_name"]
            )
        )
    if "code_repository_provider_type" in value:
        import capo_inspector2.types.string_filter_list

        out["codeRepositoryProviderType"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["code_repository_provider_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if "findingArn" in data:
        import capo_inspector2.types.string_filter_list

        out["finding_arn"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["findingArn"]
        )
    if "awsAccountId" in data:
        import capo_inspector2.types.string_filter_list

        out["aws_account_id"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["awsAccountId"]
            )
        )
    if "findingType" in data:
        import capo_inspector2.types.string_filter_list

        out["finding_type"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["findingType"]
        )
    if "severity" in data:
        import capo_inspector2.types.string_filter_list

        out["severity"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["severity"]
        )
    if "firstObservedAt" in data:
        import capo_inspector2.types.date_filter_list

        out["first_observed_at"] = (
            capo_inspector2.types.date_filter_list.deserialize_json(
                data["firstObservedAt"]
            )
        )
    if "lastObservedAt" in data:
        import capo_inspector2.types.date_filter_list

        out["last_observed_at"] = (
            capo_inspector2.types.date_filter_list.deserialize_json(
                data["lastObservedAt"]
            )
        )
    if "updatedAt" in data:
        import capo_inspector2.types.date_filter_list

        out["updated_at"] = capo_inspector2.types.date_filter_list.deserialize_json(
            data["updatedAt"]
        )
    if "findingStatus" in data:
        import capo_inspector2.types.string_filter_list

        out["finding_status"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["findingStatus"]
            )
        )
    if "title" in data:
        import capo_inspector2.types.string_filter_list

        out["title"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["title"]
        )
    if "inspectorScore" in data:
        import capo_inspector2.types.number_filter_list

        out["inspector_score"] = (
            capo_inspector2.types.number_filter_list.deserialize_json(
                data["inspectorScore"]
            )
        )
    if "resourceType" in data:
        import capo_inspector2.types.string_filter_list

        out["resource_type"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["resourceType"]
            )
        )
    if "resourceId" in data:
        import capo_inspector2.types.string_filter_list

        out["resource_id"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["resourceId"]
        )
    if "resourceTags" in data:
        import capo_inspector2.types.map_filter_list

        out["resource_tags"] = capo_inspector2.types.map_filter_list.deserialize_json(
            data["resourceTags"]
        )
    if "ec2InstanceImageId" in data:
        import capo_inspector2.types.string_filter_list

        out["ec2_instance_image_id"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ec2InstanceImageId"]
            )
        )
    if "ec2InstanceVpcId" in data:
        import capo_inspector2.types.string_filter_list

        out["ec2_instance_vpc_id"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ec2InstanceVpcId"]
            )
        )
    if "ec2InstanceSubnetId" in data:
        import capo_inspector2.types.string_filter_list

        out["ec2_instance_subnet_id"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ec2InstanceSubnetId"]
            )
        )
    if "ecrImagePushedAt" in data:
        import capo_inspector2.types.date_filter_list

        out["ecr_image_pushed_at"] = (
            capo_inspector2.types.date_filter_list.deserialize_json(
                data["ecrImagePushedAt"]
            )
        )
    if "ecrImageArchitecture" in data:
        import capo_inspector2.types.string_filter_list

        out["ecr_image_architecture"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageArchitecture"]
            )
        )
    if "ecrImageRegistry" in data:
        import capo_inspector2.types.string_filter_list

        out["ecr_image_registry"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageRegistry"]
            )
        )
    if "ecrImageRepositoryName" in data:
        import capo_inspector2.types.string_filter_list

        out["ecr_image_repository_name"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageRepositoryName"]
            )
        )
    if "ecrImageTags" in data:
        import capo_inspector2.types.string_filter_list

        out["ecr_image_tags"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageTags"]
            )
        )
    if "ecrImageHash" in data:
        import capo_inspector2.types.string_filter_list

        out["ecr_image_hash"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageHash"]
            )
        )
    if "ecrImageLastInUseAt" in data:
        import capo_inspector2.types.date_filter_list

        out["ecr_image_last_in_use_at"] = (
            capo_inspector2.types.date_filter_list.deserialize_json(
                data["ecrImageLastInUseAt"]
            )
        )
    if "ecrImageInUseCount" in data:
        import capo_inspector2.types.number_filter_list

        out["ecr_image_in_use_count"] = (
            capo_inspector2.types.number_filter_list.deserialize_json(
                data["ecrImageInUseCount"]
            )
        )
    if "portRange" in data:
        import capo_inspector2.types.port_range_filter_list

        out["port_range"] = (
            capo_inspector2.types.port_range_filter_list.deserialize_json(
                data["portRange"]
            )
        )
    if "networkProtocol" in data:
        import capo_inspector2.types.string_filter_list

        out["network_protocol"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["networkProtocol"]
            )
        )
    if "componentId" in data:
        import capo_inspector2.types.string_filter_list

        out["component_id"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["componentId"]
        )
    if "componentType" in data:
        import capo_inspector2.types.string_filter_list

        out["component_type"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["componentType"]
            )
        )
    if "vulnerabilityId" in data:
        import capo_inspector2.types.string_filter_list

        out["vulnerability_id"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["vulnerabilityId"]
            )
        )
    if "vulnerabilitySource" in data:
        import capo_inspector2.types.string_filter_list

        out["vulnerability_source"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["vulnerabilitySource"]
            )
        )
    if "vendorSeverity" in data:
        import capo_inspector2.types.string_filter_list

        out["vendor_severity"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["vendorSeverity"]
            )
        )
    if "vulnerablePackages" in data:
        import capo_inspector2.types.package_filter_list

        out["vulnerable_packages"] = (
            capo_inspector2.types.package_filter_list.deserialize_json(
                data["vulnerablePackages"]
            )
        )
    if "relatedVulnerabilities" in data:
        import capo_inspector2.types.string_filter_list

        out["related_vulnerabilities"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["relatedVulnerabilities"]
            )
        )
    if "fixAvailable" in data:
        import capo_inspector2.types.string_filter_list

        out["fix_available"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["fixAvailable"]
            )
        )
    if "lambdaFunctionName" in data:
        import capo_inspector2.types.string_filter_list

        out["lambda_function_name"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionName"]
            )
        )
    if "lambdaFunctionLayers" in data:
        import capo_inspector2.types.string_filter_list

        out["lambda_function_layers"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionLayers"]
            )
        )
    if "lambdaFunctionRuntime" in data:
        import capo_inspector2.types.string_filter_list

        out["lambda_function_runtime"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionRuntime"]
            )
        )
    if "lambdaFunctionLastModifiedAt" in data:
        import capo_inspector2.types.date_filter_list

        out["lambda_function_last_modified_at"] = (
            capo_inspector2.types.date_filter_list.deserialize_json(
                data["lambdaFunctionLastModifiedAt"]
            )
        )
    if "lambdaFunctionExecutionRoleArn" in data:
        import capo_inspector2.types.string_filter_list

        out["lambda_function_execution_role_arn"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionExecutionRoleArn"]
            )
        )
    if "exploitAvailable" in data:
        import capo_inspector2.types.string_filter_list

        out["exploit_available"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["exploitAvailable"]
            )
        )
    if "codeVulnerabilityDetectorName" in data:
        import capo_inspector2.types.string_filter_list

        out["code_vulnerability_detector_name"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["codeVulnerabilityDetectorName"]
            )
        )
    if "codeVulnerabilityDetectorTags" in data:
        import capo_inspector2.types.string_filter_list

        out["code_vulnerability_detector_tags"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["codeVulnerabilityDetectorTags"]
            )
        )
    if "codeVulnerabilityFilePath" in data:
        import capo_inspector2.types.string_filter_list

        out["code_vulnerability_file_path"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["codeVulnerabilityFilePath"]
            )
        )
    if "epssScore" in data:
        import capo_inspector2.types.number_filter_list

        out["epss_score"] = capo_inspector2.types.number_filter_list.deserialize_json(
            data["epssScore"]
        )
    if "codeRepositoryProjectName" in data:
        import capo_inspector2.types.string_filter_list

        out["code_repository_project_name"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["codeRepositoryProjectName"]
            )
        )
    if "codeRepositoryProviderType" in data:
        import capo_inspector2.types.string_filter_list

        out["code_repository_provider_type"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["codeRepositoryProviderType"]
            )
        )
    return out
