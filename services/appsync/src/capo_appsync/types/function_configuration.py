"""Generated from Smithy shape ``com.amazonaws.appsync#FunctionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.app_sync_runtime
    import capo_appsync.types.code
    import capo_appsync.types.mapping_template
    import capo_appsync.types.max_batch_size
    import capo_appsync.types.resource_name
    import capo_appsync.types.string
    import capo_appsync.types.sync_config


class FunctionConfiguration(TypedDict, closed=True):
    function_id: NotRequired["capo_appsync.types.string.String"]
    """<p>A unique ID representing the <code>Function</code> object.</p>"""
    function_arn: NotRequired["capo_appsync.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the <code>Function</code> object.</p>"""
    name: NotRequired["capo_appsync.types.resource_name.ResourceName"]
    """<p>The name of the <code>Function</code> object.</p>"""
    description: NotRequired["capo_appsync.types.string.String"]
    """<p>The <code>Function</code> description.</p>"""
    data_source_name: NotRequired["capo_appsync.types.resource_name.ResourceName"]
    """<p>The name of the <code>DataSource</code>.</p>"""
    request_mapping_template: NotRequired[
        "capo_appsync.types.mapping_template.MappingTemplate"
    ]
    """<p>The <code>Function</code> request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p>"""
    response_mapping_template: NotRequired[
        "capo_appsync.types.mapping_template.MappingTemplate"
    ]
    """<p>The <code>Function</code> response mapping template.</p>"""
    function_version: NotRequired["capo_appsync.types.string.String"]
    """<p>The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.</p>"""
    sync_config: NotRequired["capo_appsync.types.sync_config.SyncConfig"]
    max_batch_size: "capo_appsync.types.max_batch_size.MaxBatchSize"
    """<p>The maximum batching size for a resolver.</p>"""
    runtime: NotRequired["capo_appsync.types.app_sync_runtime.AppSyncRuntime"]
    code: NotRequired["capo_appsync.types.code.Code"]
    """<p>The <code>function</code> code that contains the request and response functions. When code is used, the <code>runtime</code> is required. The <code>runtime</code> value must be <code>APPSYNC_JS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionConfiguration) -> dict:
    out: dict = {}
    if "function_id" in value:
        out["functionId"] = value["function_id"]
    if "function_arn" in value:
        out["functionArn"] = value["function_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "data_source_name" in value:
        out["dataSourceName"] = value["data_source_name"]
    if "request_mapping_template" in value:
        out["requestMappingTemplate"] = value["request_mapping_template"]
    if "response_mapping_template" in value:
        out["responseMappingTemplate"] = value["response_mapping_template"]
    if "function_version" in value:
        out["functionVersion"] = value["function_version"]
    if "sync_config" in value:
        import capo_appsync.types.sync_config

        out["syncConfig"] = capo_appsync.types.sync_config.serialize_json(
            value["sync_config"]
        )
    out["maxBatchSize"] = value.get("max_batch_size", 0)
    if "runtime" in value:
        import capo_appsync.types.app_sync_runtime

        out["runtime"] = capo_appsync.types.app_sync_runtime.serialize_json(
            value["runtime"]
        )
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> FunctionConfiguration:
    out: FunctionConfiguration = {}  # type: ignore[typeddict-item]
    if "functionId" in data:
        out["function_id"] = data["functionId"]
    if "functionArn" in data:
        out["function_arn"] = data["functionArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "dataSourceName" in data:
        out["data_source_name"] = data["dataSourceName"]
    if "requestMappingTemplate" in data:
        out["request_mapping_template"] = data["requestMappingTemplate"]
    if "responseMappingTemplate" in data:
        out["response_mapping_template"] = data["responseMappingTemplate"]
    if "functionVersion" in data:
        out["function_version"] = data["functionVersion"]
    if "syncConfig" in data:
        import capo_appsync.types.sync_config

        out["sync_config"] = capo_appsync.types.sync_config.deserialize_json(
            data["syncConfig"]
        )
    if "maxBatchSize" in data:
        out["max_batch_size"] = data["maxBatchSize"]
    else:
        out["max_batch_size"] = 0
    if "runtime" in data:
        import capo_appsync.types.app_sync_runtime

        out["runtime"] = capo_appsync.types.app_sync_runtime.deserialize_json(
            data["runtime"]
        )
    if "code" in data:
        out["code"] = data["code"]
    return out
