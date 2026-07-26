"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeNodeFromTemplateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.created_time
    import capo_panorama.types.description
    import capo_panorama.types.job_id
    import capo_panorama.types.job_tags_list
    import capo_panorama.types.last_updated_time
    import capo_panorama.types.node_from_template_job_status
    import capo_panorama.types.node_from_template_job_status_message
    import capo_panorama.types.node_name
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_version
    import capo_panorama.types.template_parameters_map
    import capo_panorama.types.template_type


class DescribeNodeFromTemplateJobResponse(TypedDict, closed=True):
    job_id: "capo_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""
    status: (
        "capo_panorama.types.node_from_template_job_status.NodeFromTemplateJobStatus"
    )
    """<p>The job's status.</p>"""
    status_message: "capo_panorama.types.node_from_template_job_status_message.NodeFromTemplateJobStatusMessage"
    """<p>The job's status message.</p>"""
    created_time: "capo_panorama.types.created_time.CreatedTime"
    """<p>When the job was created.</p>"""
    last_updated_time: "capo_panorama.types.last_updated_time.LastUpdatedTime"
    """<p>When the job was updated.</p>"""
    output_package_name: "capo_panorama.types.node_package_name.NodePackageName"
    """<p>The job's output package name.</p>"""
    output_package_version: (
        "capo_panorama.types.node_package_version.NodePackageVersion"
    )
    """<p>The job's output package version.</p>"""
    node_name: "capo_panorama.types.node_name.NodeName"
    """<p>The node's name.</p>"""
    node_description: NotRequired["capo_panorama.types.description.Description"]
    """<p>The node's description.</p>"""
    template_type: "capo_panorama.types.template_type.TemplateType"
    """<p>The job's template type.</p>"""
    template_parameters: (
        "capo_panorama.types.template_parameters_map.TemplateParametersMap"
    )
    """<p>The job's template parameters.</p>"""
    job_tags: NotRequired["capo_panorama.types.job_tags_list.JobTagsList"]
    """<p>The job's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNodeFromTemplateJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    out["Status"] = value["status"]
    out["StatusMessage"] = value["status_message"]
    import capo_panorama.types.created_time

    out["CreatedTime"] = capo_panorama.types.created_time.serialize_json(
        value["created_time"]
    )
    import capo_panorama.types.last_updated_time

    out["LastUpdatedTime"] = capo_panorama.types.last_updated_time.serialize_json(
        value["last_updated_time"]
    )
    out["OutputPackageName"] = value["output_package_name"]
    out["OutputPackageVersion"] = value["output_package_version"]
    out["NodeName"] = value["node_name"]
    if "node_description" in value:
        out["NodeDescription"] = value["node_description"]
    out["TemplateType"] = value["template_type"]
    import capo_panorama.types.template_parameters_map

    out["TemplateParameters"] = (
        capo_panorama.types.template_parameters_map.serialize_json(
            value["template_parameters"]
        )
    )
    if "job_tags" in value:
        import capo_panorama.types.job_tags_list

        out["JobTags"] = capo_panorama.types.job_tags_list.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribeNodeFromTemplateJobResponse:
    out: DescribeNodeFromTemplateJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.job_id required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.status required"
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.status_message required"
        )
    if "CreatedTime" in data:
        import capo_panorama.types.created_time

        out["created_time"] = capo_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.created_time required"
        )
    if "LastUpdatedTime" in data:
        import capo_panorama.types.last_updated_time

        out["last_updated_time"] = (
            capo_panorama.types.last_updated_time.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.last_updated_time required"
        )
    if "OutputPackageName" in data:
        out["output_package_name"] = data["OutputPackageName"]
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.output_package_name required"
        )
    if "OutputPackageVersion" in data:
        out["output_package_version"] = data["OutputPackageVersion"]
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.output_package_version required"
        )
    if "NodeName" in data:
        out["node_name"] = data["NodeName"]
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.node_name required"
        )
    if "NodeDescription" in data:
        out["node_description"] = data["NodeDescription"]
    if "TemplateType" in data:
        out["template_type"] = data["TemplateType"]
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.template_type required"
        )
    if "TemplateParameters" in data:
        import capo_panorama.types.template_parameters_map

        out["template_parameters"] = (
            capo_panorama.types.template_parameters_map.deserialize_json(
                data["TemplateParameters"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeNodeFromTemplateJobResponse.template_parameters required"
        )
    if "JobTags" in data:
        import capo_panorama.types.job_tags_list

        out["job_tags"] = capo_panorama.types.job_tags_list.deserialize_json(
            data["JobTags"]
        )
    return out
