"""Generated from Smithy shape ``com.amazonaws.dlm#Script``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.execute_operation_on_script_failure
    import capo_dlm.types.execution_handler
    import capo_dlm.types.execution_handler_service_values
    import capo_dlm.types.script_execution_timeout
    import capo_dlm.types.script_maximum_retry_count
    import capo_dlm.types.stages_list


class Script(TypedDict, closed=True):
    stages: NotRequired["capo_dlm.types.stages_list.StagesList"]
    """<p>Indicate which scripts Amazon Data Lifecycle Manager should run on target instances. Pre scripts run before Amazon Data Lifecycle Manager initiates snapshot creation. Post scripts run after Amazon Data Lifecycle Manager initiates snapshot creation.</p> <ul> <li> <p>To run a pre script only, specify <code>PRE</code>. In this case, Amazon Data Lifecycle Manager calls the SSM document with the <code>pre-script</code> parameter before initiating snapshot creation.</p> </li> <li> <p>To run a post script only, specify <code>POST</code>. In this case, Amazon Data Lifecycle Manager calls the SSM document with the <code>post-script</code> parameter after initiating snapshot creation.</p> </li> <li> <p>To run both pre and post scripts, specify both <code>PRE</code> and <code>POST</code>. In this case, Amazon Data Lifecycle Manager calls the SSM document with the <code>pre-script</code> parameter before initiating snapshot creation, and then it calls the SSM document again with the <code>post-script</code> parameter after initiating snapshot creation.</p> </li> </ul> <p>If you are automating VSS Backups, omit this parameter.</p> <p>Default: PRE and POST</p>"""
    execution_handler_service: NotRequired[
        "capo_dlm.types.execution_handler_service_values.ExecutionHandlerServiceValues"
    ]
    """<p>Indicates the service used to execute the pre and/or post scripts.</p> <ul> <li> <p>If you are using custom SSM documents or automating application-consistent snapshots of SAP HANA workloads, specify <code>AWS_SYSTEMS_MANAGER</code>.</p> </li> <li> <p>If you are automating VSS Backups, omit this parameter.</p> </li> </ul> <p>Default: AWS_SYSTEMS_MANAGER</p>"""
    execution_handler: NotRequired["capo_dlm.types.execution_handler.ExecutionHandler"]
    """<p>The SSM document that includes the pre and/or post scripts to run.</p> <ul> <li> <p>If you are automating VSS backups, specify <code>AWS_VSS_BACKUP</code>. In this case, Amazon Data Lifecycle Manager automatically uses the <code>AWSEC2-CreateVssSnapshot</code> SSM document.</p> </li> <li> <p>If you are automating application-consistent snapshots for SAP HANA workloads, specify <code>AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA</code>.</p> </li> <li> <p>If you are using a custom SSM document that you own, specify either the name or ARN of the SSM document. If you are using a custom SSM document that is shared with you, specify the ARN of the SSM document.</p> </li> </ul>"""
    execute_operation_on_script_failure: NotRequired[
        "capo_dlm.types.execute_operation_on_script_failure.ExecuteOperationOnScriptFailure"
    ]
    """<p>Indicates whether Amazon Data Lifecycle Manager should default to crash-consistent snapshots if the pre script fails.</p> <ul> <li> <p>To default to crash consistent snapshot if the pre script fails, specify <code>true</code>.</p> </li> <li> <p>To skip the instance for snapshot creation if the pre script fails, specify <code>false</code>.</p> </li> </ul> <p>This parameter is supported only if you run a pre script. If you run a post script only, omit this parameter.</p> <p>Default: true</p>"""
    execution_timeout: NotRequired[
        "capo_dlm.types.script_execution_timeout.ScriptExecutionTimeout"
    ]
    """<p>Specifies a timeout period, in seconds, after which Amazon Data Lifecycle Manager fails the script run attempt if it has not completed. If a script does not complete within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies to the pre and post scripts individually. </p> <p>If you are automating VSS Backups, omit this parameter.</p> <p>Default: 10</p>"""
    maximum_retry_count: NotRequired[
        "capo_dlm.types.script_maximum_retry_count.ScriptMaximumRetryCount"
    ]
    """<p>Specifies the number of times Amazon Data Lifecycle Manager should retry scripts that fail.</p> <ul> <li> <p>If the pre script fails, Amazon Data Lifecycle Manager retries the entire snapshot creation process, including running the pre and post scripts.</p> </li> <li> <p>If the post script fails, Amazon Data Lifecycle Manager retries the post script only; in this case, the pre script will have completed and the snapshot might have been created.</p> </li> </ul> <p>If you do not want Amazon Data Lifecycle Manager to retry failed scripts, specify <code>0</code>.</p> <p>Default: 0</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Script) -> dict:
    out: dict = {}
    if "stages" in value:
        import capo_dlm.types.stages_list

        out["Stages"] = capo_dlm.types.stages_list.serialize_json(value["stages"])
    if "execution_handler_service" in value:
        import capo_dlm.types.execution_handler_service_values

        out["ExecutionHandlerService"] = (
            capo_dlm.types.execution_handler_service_values.serialize_json(
                value["execution_handler_service"]
            )
        )
    if "execution_handler" in value:
        out["ExecutionHandler"] = value["execution_handler"]
    if "execute_operation_on_script_failure" in value:
        out["ExecuteOperationOnScriptFailure"] = value[
            "execute_operation_on_script_failure"
        ]
    if "execution_timeout" in value:
        out["ExecutionTimeout"] = value["execution_timeout"]
    if "maximum_retry_count" in value:
        out["MaximumRetryCount"] = value["maximum_retry_count"]
    return out


def deserialize_json(data: dict) -> Script:
    out: Script = {}  # type: ignore[typeddict-item]
    if "Stages" in data:
        import capo_dlm.types.stages_list

        out["stages"] = capo_dlm.types.stages_list.deserialize_json(data["Stages"])
    if "ExecutionHandlerService" in data:
        import capo_dlm.types.execution_handler_service_values

        out["execution_handler_service"] = (
            capo_dlm.types.execution_handler_service_values.deserialize_json(
                data["ExecutionHandlerService"]
            )
        )
    if "ExecutionHandler" in data:
        out["execution_handler"] = data["ExecutionHandler"]
    if "ExecuteOperationOnScriptFailure" in data:
        out["execute_operation_on_script_failure"] = data[
            "ExecuteOperationOnScriptFailure"
        ]
    if "ExecutionTimeout" in data:
        out["execution_timeout"] = data["ExecutionTimeout"]
    if "MaximumRetryCount" in data:
        out["maximum_retry_count"] = data["MaximumRetryCount"]
    return out
