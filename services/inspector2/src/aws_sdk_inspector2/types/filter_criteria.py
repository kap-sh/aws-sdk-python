"""Generated from Smithy shape ``com.amazonaws.inspector2#FilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.date_filter_list
    import aws_sdk_inspector2.types.map_filter_list
    import aws_sdk_inspector2.types.number_filter_list
    import aws_sdk_inspector2.types.package_filter_list
    import aws_sdk_inspector2.types.port_range_filter_list
    import aws_sdk_inspector2.types.string_filter_list


class FilterCriteria(TypedDict):
    finding_arn: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the finding ARNs used to filter findings.</p>"""
    aws_account_id: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon Web Services account IDs used to filter findings.</p>"""
    finding_type: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the finding types used to filter findings.</p>"""
    severity: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the severity used to filter findings.</p>"""
    first_observed_at: NotRequired[
        "aws_sdk_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Details on the date and time a finding was first seen used to filter findings.</p>"""
    last_observed_at: NotRequired[
        "aws_sdk_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Details on the date and time a finding was last seen used to filter findings.</p>"""
    updated_at: NotRequired["aws_sdk_inspector2.types.date_filter_list.DateFilterList"]
    """<p>Details on the date and time a finding was last updated at used to filter findings.</p>"""
    finding_status: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the finding status types used to filter findings.</p>"""
    title: NotRequired["aws_sdk_inspector2.types.string_filter_list.StringFilterList"]
    """<p>Details on the finding title used to filter findings.</p>"""
    inspector_score: NotRequired[
        "aws_sdk_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>The Amazon Inspector score to filter on.</p>"""
    resource_type: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the resource types used to filter findings.</p>"""
    resource_id: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the resource IDs used to filter findings.</p>"""
    resource_tags: NotRequired["aws_sdk_inspector2.types.map_filter_list.MapFilterList"]
    """<p>Details on the resource tags used to filter findings.</p>"""
    ec2_instance_image_id: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon EC2 instance image IDs used to filter findings.</p>"""
    ec2_instance_vpc_id: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon EC2 instance VPC IDs used to filter findings.</p>"""
    ec2_instance_subnet_id: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon EC2 instance subnet IDs used to filter findings.</p>"""
    ecr_image_pushed_at: NotRequired[
        "aws_sdk_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Details on the Amazon ECR image push date and time used to filter findings.</p>"""
    ecr_image_architecture: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon ECR image architecture types used to filter findings.</p>"""
    ecr_image_registry: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the Amazon ECR registry used to filter findings.</p>"""
    ecr_image_repository_name: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the name of the Amazon ECR repository used to filter findings.</p>"""
    ecr_image_tags: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The tags attached to the Amazon ECR container image.</p>"""
    ecr_image_hash: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the Amazon ECR image hashes used to filter findings.</p>"""
    ecr_image_last_in_use_at: NotRequired[
        "aws_sdk_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Filter criteria indicating when an Amazon ECR image was last used in an Amazon ECS cluster task or Amazon EKS cluster pod.</p>"""
    ecr_image_in_use_count: NotRequired[
        "aws_sdk_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>Filter criteria indicating when details for an Amazon ECR image include when an Amazon ECR image is in use.</p>"""
    port_range: NotRequired[
        "aws_sdk_inspector2.types.port_range_filter_list.PortRangeFilterList"
    ]
    """<p>Details on the port ranges used to filter findings.</p>"""
    network_protocol: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on network protocol used to filter findings.</p>"""
    component_id: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the component IDs used to filter findings.</p>"""
    component_type: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details of the component types used to filter findings.</p>"""
    vulnerability_id: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the vulnerability ID used to filter findings.</p>"""
    vulnerability_source: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the vulnerability type used to filter findings.</p>"""
    vendor_severity: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the vendor severity used to filter findings.</p>"""
    vulnerable_packages: NotRequired[
        "aws_sdk_inspector2.types.package_filter_list.PackageFilterList"
    ]
    """<p>Details on the vulnerable packages used to filter findings.</p>"""
    related_vulnerabilities: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on the related vulnerabilities used to filter findings.</p>"""
    fix_available: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Details on whether a fix is available through a version update. This value can be <code>YES</code>, <code>NO</code>, or <code>PARTIAL</code>. A <code>PARTIAL</code> fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.</p>"""
    lambda_function_name: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by the name of the function.</p>"""
    lambda_function_layers: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\"> layers</a>. A Lambda function can have up to five layers.</p>"""
    lambda_function_runtime: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by the runtime environment for the Lambda function.</p>"""
    lambda_function_last_modified_at: NotRequired[
        "aws_sdk_inspector2.types.date_filter_list.DateFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by the date and time that a user last updated the configuration, in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601 format</a> </p>"""
    lambda_function_execution_role_arn: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda functions by execution role.</p>"""
    exploit_available: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filters the list of Amazon Web Services Lambda findings by the availability of exploits.</p>"""
    code_vulnerability_detector_name: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The name of the detector used to identify a code vulnerability in a Lambda function used to filter findings.</p>"""
    code_vulnerability_detector_tags: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The detector type tag associated with the vulnerability used to filter findings. Detector tags group related vulnerabilities by common themes or tactics. For a list of available tags by programming language, see <a href=\"https://docs.aws.amazon.com/codeguru/detector-library/java/tags/\">Java tags</a>, or <a href=\"https://docs.aws.amazon.com/codeguru/detector-library/python/tags/\">Python tags</a>. </p>"""
    code_vulnerability_file_path: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The file path to the file in a Lambda function that contains a code vulnerability used to filter findings.</p>"""
    epss_score: NotRequired[
        "aws_sdk_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>The EPSS score used to filter findings.</p>"""
    code_repository_project_name: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filter criteria for findings based on the project name in a code repository.</p>"""
    code_repository_provider_type: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>Filter criteria for findings based on the repository provider type (such as GitHub, GitLab, etc.).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "finding_arn" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["findingArn"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["finding_arn"]
        )
    if "aws_account_id" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["awsAccountId"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["aws_account_id"]
            )
        )
    if "finding_type" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["findingType"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["finding_type"]
        )
    if "severity" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["severity"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["severity"]
        )
    if "first_observed_at" in value:
        import aws_sdk_inspector2.types.date_filter_list

        out["firstObservedAt"] = (
            aws_sdk_inspector2.types.date_filter_list.serialize_json(
                value["first_observed_at"]
            )
        )
    if "last_observed_at" in value:
        import aws_sdk_inspector2.types.date_filter_list

        out["lastObservedAt"] = (
            aws_sdk_inspector2.types.date_filter_list.serialize_json(
                value["last_observed_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_inspector2.types.date_filter_list

        out["updatedAt"] = aws_sdk_inspector2.types.date_filter_list.serialize_json(
            value["updated_at"]
        )
    if "finding_status" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["findingStatus"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["finding_status"]
            )
        )
    if "title" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["title"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["title"]
        )
    if "inspector_score" in value:
        import aws_sdk_inspector2.types.number_filter_list

        out["inspectorScore"] = (
            aws_sdk_inspector2.types.number_filter_list.serialize_json(
                value["inspector_score"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["resourceType"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["resourceId"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["resource_id"]
        )
    if "resource_tags" in value:
        import aws_sdk_inspector2.types.map_filter_list

        out["resourceTags"] = aws_sdk_inspector2.types.map_filter_list.serialize_json(
            value["resource_tags"]
        )
    if "ec2_instance_image_id" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ec2InstanceImageId"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ec2_instance_image_id"]
            )
        )
    if "ec2_instance_vpc_id" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ec2InstanceVpcId"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ec2_instance_vpc_id"]
            )
        )
    if "ec2_instance_subnet_id" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ec2InstanceSubnetId"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ec2_instance_subnet_id"]
            )
        )
    if "ecr_image_pushed_at" in value:
        import aws_sdk_inspector2.types.date_filter_list

        out["ecrImagePushedAt"] = (
            aws_sdk_inspector2.types.date_filter_list.serialize_json(
                value["ecr_image_pushed_at"]
            )
        )
    if "ecr_image_architecture" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecrImageArchitecture"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_architecture"]
            )
        )
    if "ecr_image_registry" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecrImageRegistry"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_registry"]
            )
        )
    if "ecr_image_repository_name" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecrImageRepositoryName"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_repository_name"]
            )
        )
    if "ecr_image_tags" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecrImageTags"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_tags"]
            )
        )
    if "ecr_image_hash" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecrImageHash"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["ecr_image_hash"]
            )
        )
    if "ecr_image_last_in_use_at" in value:
        import aws_sdk_inspector2.types.date_filter_list

        out["ecrImageLastInUseAt"] = (
            aws_sdk_inspector2.types.date_filter_list.serialize_json(
                value["ecr_image_last_in_use_at"]
            )
        )
    if "ecr_image_in_use_count" in value:
        import aws_sdk_inspector2.types.number_filter_list

        out["ecrImageInUseCount"] = (
            aws_sdk_inspector2.types.number_filter_list.serialize_json(
                value["ecr_image_in_use_count"]
            )
        )
    if "port_range" in value:
        import aws_sdk_inspector2.types.port_range_filter_list

        out["portRange"] = (
            aws_sdk_inspector2.types.port_range_filter_list.serialize_json(
                value["port_range"]
            )
        )
    if "network_protocol" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["networkProtocol"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["network_protocol"]
            )
        )
    if "component_id" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["componentId"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["component_id"]
        )
    if "component_type" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["componentType"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["component_type"]
            )
        )
    if "vulnerability_id" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["vulnerabilityId"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["vulnerability_id"]
            )
        )
    if "vulnerability_source" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["vulnerabilitySource"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["vulnerability_source"]
            )
        )
    if "vendor_severity" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["vendorSeverity"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["vendor_severity"]
            )
        )
    if "vulnerable_packages" in value:
        import aws_sdk_inspector2.types.package_filter_list

        out["vulnerablePackages"] = (
            aws_sdk_inspector2.types.package_filter_list.serialize_json(
                value["vulnerable_packages"]
            )
        )
    if "related_vulnerabilities" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["relatedVulnerabilities"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["related_vulnerabilities"]
            )
        )
    if "fix_available" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["fixAvailable"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["fix_available"]
            )
        )
    if "lambda_function_name" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambdaFunctionName"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_name"]
            )
        )
    if "lambda_function_layers" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambdaFunctionLayers"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_layers"]
            )
        )
    if "lambda_function_runtime" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambdaFunctionRuntime"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_runtime"]
            )
        )
    if "lambda_function_last_modified_at" in value:
        import aws_sdk_inspector2.types.date_filter_list

        out["lambdaFunctionLastModifiedAt"] = (
            aws_sdk_inspector2.types.date_filter_list.serialize_json(
                value["lambda_function_last_modified_at"]
            )
        )
    if "lambda_function_execution_role_arn" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambdaFunctionExecutionRoleArn"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["lambda_function_execution_role_arn"]
            )
        )
    if "exploit_available" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["exploitAvailable"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["exploit_available"]
            )
        )
    if "code_vulnerability_detector_name" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["codeVulnerabilityDetectorName"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["code_vulnerability_detector_name"]
            )
        )
    if "code_vulnerability_detector_tags" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["codeVulnerabilityDetectorTags"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["code_vulnerability_detector_tags"]
            )
        )
    if "code_vulnerability_file_path" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["codeVulnerabilityFilePath"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["code_vulnerability_file_path"]
            )
        )
    if "epss_score" in value:
        import aws_sdk_inspector2.types.number_filter_list

        out["epssScore"] = aws_sdk_inspector2.types.number_filter_list.serialize_json(
            value["epss_score"]
        )
    if "code_repository_project_name" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["codeRepositoryProjectName"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["code_repository_project_name"]
            )
        )
    if "code_repository_provider_type" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["codeRepositoryProviderType"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["code_repository_provider_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if "findingArn" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["finding_arn"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["findingArn"]
            )
        )
    if "awsAccountId" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["aws_account_id"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["awsAccountId"]
            )
        )
    if "findingType" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["finding_type"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["findingType"]
            )
        )
    if "severity" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["severity"] = aws_sdk_inspector2.types.string_filter_list.deserialize_json(
            data["severity"]
        )
    if "firstObservedAt" in data:
        import aws_sdk_inspector2.types.date_filter_list

        out["first_observed_at"] = (
            aws_sdk_inspector2.types.date_filter_list.deserialize_json(
                data["firstObservedAt"]
            )
        )
    if "lastObservedAt" in data:
        import aws_sdk_inspector2.types.date_filter_list

        out["last_observed_at"] = (
            aws_sdk_inspector2.types.date_filter_list.deserialize_json(
                data["lastObservedAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_inspector2.types.date_filter_list

        out["updated_at"] = aws_sdk_inspector2.types.date_filter_list.deserialize_json(
            data["updatedAt"]
        )
    if "findingStatus" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["finding_status"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["findingStatus"]
            )
        )
    if "title" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["title"] = aws_sdk_inspector2.types.string_filter_list.deserialize_json(
            data["title"]
        )
    if "inspectorScore" in data:
        import aws_sdk_inspector2.types.number_filter_list

        out["inspector_score"] = (
            aws_sdk_inspector2.types.number_filter_list.deserialize_json(
                data["inspectorScore"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["resource_type"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["resourceType"]
            )
        )
    if "resourceId" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["resource_id"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["resourceId"]
            )
        )
    if "resourceTags" in data:
        import aws_sdk_inspector2.types.map_filter_list

        out["resource_tags"] = (
            aws_sdk_inspector2.types.map_filter_list.deserialize_json(
                data["resourceTags"]
            )
        )
    if "ec2InstanceImageId" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ec2_instance_image_id"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ec2InstanceImageId"]
            )
        )
    if "ec2InstanceVpcId" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ec2_instance_vpc_id"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ec2InstanceVpcId"]
            )
        )
    if "ec2InstanceSubnetId" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ec2_instance_subnet_id"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ec2InstanceSubnetId"]
            )
        )
    if "ecrImagePushedAt" in data:
        import aws_sdk_inspector2.types.date_filter_list

        out["ecr_image_pushed_at"] = (
            aws_sdk_inspector2.types.date_filter_list.deserialize_json(
                data["ecrImagePushedAt"]
            )
        )
    if "ecrImageArchitecture" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecr_image_architecture"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageArchitecture"]
            )
        )
    if "ecrImageRegistry" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecr_image_registry"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageRegistry"]
            )
        )
    if "ecrImageRepositoryName" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecr_image_repository_name"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageRepositoryName"]
            )
        )
    if "ecrImageTags" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecr_image_tags"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageTags"]
            )
        )
    if "ecrImageHash" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["ecr_image_hash"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["ecrImageHash"]
            )
        )
    if "ecrImageLastInUseAt" in data:
        import aws_sdk_inspector2.types.date_filter_list

        out["ecr_image_last_in_use_at"] = (
            aws_sdk_inspector2.types.date_filter_list.deserialize_json(
                data["ecrImageLastInUseAt"]
            )
        )
    if "ecrImageInUseCount" in data:
        import aws_sdk_inspector2.types.number_filter_list

        out["ecr_image_in_use_count"] = (
            aws_sdk_inspector2.types.number_filter_list.deserialize_json(
                data["ecrImageInUseCount"]
            )
        )
    if "portRange" in data:
        import aws_sdk_inspector2.types.port_range_filter_list

        out["port_range"] = (
            aws_sdk_inspector2.types.port_range_filter_list.deserialize_json(
                data["portRange"]
            )
        )
    if "networkProtocol" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["network_protocol"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["networkProtocol"]
            )
        )
    if "componentId" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["component_id"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["componentId"]
            )
        )
    if "componentType" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["component_type"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["componentType"]
            )
        )
    if "vulnerabilityId" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["vulnerability_id"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["vulnerabilityId"]
            )
        )
    if "vulnerabilitySource" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["vulnerability_source"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["vulnerabilitySource"]
            )
        )
    if "vendorSeverity" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["vendor_severity"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["vendorSeverity"]
            )
        )
    if "vulnerablePackages" in data:
        import aws_sdk_inspector2.types.package_filter_list

        out["vulnerable_packages"] = (
            aws_sdk_inspector2.types.package_filter_list.deserialize_json(
                data["vulnerablePackages"]
            )
        )
    if "relatedVulnerabilities" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["related_vulnerabilities"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["relatedVulnerabilities"]
            )
        )
    if "fixAvailable" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["fix_available"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["fixAvailable"]
            )
        )
    if "lambdaFunctionName" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambda_function_name"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionName"]
            )
        )
    if "lambdaFunctionLayers" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambda_function_layers"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionLayers"]
            )
        )
    if "lambdaFunctionRuntime" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambda_function_runtime"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionRuntime"]
            )
        )
    if "lambdaFunctionLastModifiedAt" in data:
        import aws_sdk_inspector2.types.date_filter_list

        out["lambda_function_last_modified_at"] = (
            aws_sdk_inspector2.types.date_filter_list.deserialize_json(
                data["lambdaFunctionLastModifiedAt"]
            )
        )
    if "lambdaFunctionExecutionRoleArn" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["lambda_function_execution_role_arn"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["lambdaFunctionExecutionRoleArn"]
            )
        )
    if "exploitAvailable" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["exploit_available"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["exploitAvailable"]
            )
        )
    if "codeVulnerabilityDetectorName" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["code_vulnerability_detector_name"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["codeVulnerabilityDetectorName"]
            )
        )
    if "codeVulnerabilityDetectorTags" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["code_vulnerability_detector_tags"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["codeVulnerabilityDetectorTags"]
            )
        )
    if "codeVulnerabilityFilePath" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["code_vulnerability_file_path"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["codeVulnerabilityFilePath"]
            )
        )
    if "epssScore" in data:
        import aws_sdk_inspector2.types.number_filter_list

        out["epss_score"] = (
            aws_sdk_inspector2.types.number_filter_list.deserialize_json(
                data["epssScore"]
            )
        )
    if "codeRepositoryProjectName" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["code_repository_project_name"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["codeRepositoryProjectName"]
            )
        )
    if "codeRepositoryProviderType" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["code_repository_provider_type"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["codeRepositoryProviderType"]
            )
        )
    return out
