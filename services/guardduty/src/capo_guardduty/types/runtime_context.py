"""Generated from Smithy shape ``com.amazonaws.guardduty#RuntimeContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.flags_list
    import capo_guardduty.types.integer
    import capo_guardduty.types.memory_regions_list
    import capo_guardduty.types.process_details
    import capo_guardduty.types.related_file_paths_list
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class RuntimeContext(TypedDict, closed=True):
    modifying_process: NotRequired[
        "capo_guardduty.types.process_details.ProcessDetails"
    ]
    """<p>Information about the process that modified the current process. This is available for multiple finding types.</p>"""
    modified_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the process modified the current process. The timestamp is in UTC date string format.</p>"""
    script_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path to the script that was executed.</p>"""
    library_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path to the new library that was loaded.</p>"""
    ld_preload_value: NotRequired["capo_guardduty.types.string.String"]
    """<p>The value of the LD_PRELOAD environment variable.</p>"""
    socket_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path to the docket socket that was accessed.</p>"""
    runc_binary_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path to the leveraged <code>runc</code> implementation.</p>"""
    release_agent_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path in the container that modified the release agent file.</p>"""
    mount_source: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path on the host that is mounted by the container.</p>"""
    mount_target: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path in the container that is mapped to the host directory.</p>"""
    file_system_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>Represents the type of mounted fileSystem.</p>"""
    flags: NotRequired["capo_guardduty.types.flags_list.FlagsList"]
    """<p>Represents options that control the behavior of a runtime operation or action. For example, a filesystem mount operation may contain a read-only flag.</p>"""
    module_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the module loaded into the kernel.</p>"""
    module_file_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path to the module loaded into the kernel.</p>"""
    module_sha256: NotRequired["capo_guardduty.types.string.String"]
    """<p>The <code>SHA256</code> hash of the module.</p>"""
    shell_history_file_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path to the modified shell history file.</p>"""
    target_process: NotRequired["capo_guardduty.types.process_details.ProcessDetails"]
    """<p>Information about the process that had its memory overwritten by the current process.</p>"""
    address_family: NotRequired["capo_guardduty.types.string.String"]
    """<p>Represents the communication protocol associated with the address. For example, the address family <code>AF_INET</code> is used for IP version of 4 protocol.</p>"""
    iana_protocol_number: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Specifies a particular protocol within the address family. Usually there is a single protocol in address families. For example, the address family <code>AF_INET</code> only has the IP protocol.</p>"""
    memory_regions: NotRequired[
        "capo_guardduty.types.memory_regions_list.MemoryRegionsList"
    ]
    """<p>Specifies the Region of a process's address space such as stack and heap.</p>"""
    tool_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>Name of the potentially suspicious tool.</p>"""
    tool_category: NotRequired["capo_guardduty.types.string.String"]
    """<p>Category that the tool belongs to. Some of the examples are Backdoor Tool, Pentest Tool, Network Scanner, and Network Sniffer.</p>"""
    service_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>Name of the security service that has been potentially disabled.</p>"""
    command_line_example: NotRequired["capo_guardduty.types.string.String"]
    """<p>Example of the command line involved in the suspicious activity.</p>"""
    threat_file_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The suspicious file path for which the threat intelligence details were found.</p>"""
    file_operation: NotRequired["capo_guardduty.types.string.String"]
    """<p>Represents the type of file operation that triggered the finding, such as Write, Delete, Rename, Link, or Symlink.</p>"""
    file_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The path of the sensitive file that was modified. Modification includes write, delete, rename, link, or symlink operations. This field is indexed for filtering.</p>"""
    related_file_paths: NotRequired[
        "capo_guardduty.types.related_file_paths_list.RelatedFilePathsList"
    ]
    """<p>All file paths modified by the same process that triggered the finding, up to a maximum of 25 paths.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeContext) -> dict:
    out: dict = {}
    if "modifying_process" in value:
        import capo_guardduty.types.process_details

        out["modifyingProcess"] = capo_guardduty.types.process_details.serialize_json(
            value["modifying_process"]
        )
    if "modified_at" in value:
        import capo_guardduty.types.timestamp

        out["modifiedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["modified_at"]
        )
    if "script_path" in value:
        out["scriptPath"] = value["script_path"]
    if "library_path" in value:
        out["libraryPath"] = value["library_path"]
    if "ld_preload_value" in value:
        out["ldPreloadValue"] = value["ld_preload_value"]
    if "socket_path" in value:
        out["socketPath"] = value["socket_path"]
    if "runc_binary_path" in value:
        out["runcBinaryPath"] = value["runc_binary_path"]
    if "release_agent_path" in value:
        out["releaseAgentPath"] = value["release_agent_path"]
    if "mount_source" in value:
        out["mountSource"] = value["mount_source"]
    if "mount_target" in value:
        out["mountTarget"] = value["mount_target"]
    if "file_system_type" in value:
        out["fileSystemType"] = value["file_system_type"]
    if "flags" in value:
        import capo_guardduty.types.flags_list

        out["flags"] = capo_guardduty.types.flags_list.serialize_json(value["flags"])
    if "module_name" in value:
        out["moduleName"] = value["module_name"]
    if "module_file_path" in value:
        out["moduleFilePath"] = value["module_file_path"]
    if "module_sha256" in value:
        out["moduleSha256"] = value["module_sha256"]
    if "shell_history_file_path" in value:
        out["shellHistoryFilePath"] = value["shell_history_file_path"]
    if "target_process" in value:
        import capo_guardduty.types.process_details

        out["targetProcess"] = capo_guardduty.types.process_details.serialize_json(
            value["target_process"]
        )
    if "address_family" in value:
        out["addressFamily"] = value["address_family"]
    if "iana_protocol_number" in value:
        out["ianaProtocolNumber"] = value["iana_protocol_number"]
    if "memory_regions" in value:
        import capo_guardduty.types.memory_regions_list

        out["memoryRegions"] = capo_guardduty.types.memory_regions_list.serialize_json(
            value["memory_regions"]
        )
    if "tool_name" in value:
        out["toolName"] = value["tool_name"]
    if "tool_category" in value:
        out["toolCategory"] = value["tool_category"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "command_line_example" in value:
        out["commandLineExample"] = value["command_line_example"]
    if "threat_file_path" in value:
        out["threatFilePath"] = value["threat_file_path"]
    if "file_operation" in value:
        out["fileOperation"] = value["file_operation"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "related_file_paths" in value:
        import capo_guardduty.types.related_file_paths_list

        out["relatedFilePaths"] = (
            capo_guardduty.types.related_file_paths_list.serialize_json(
                value["related_file_paths"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuntimeContext:
    out: RuntimeContext = {}  # type: ignore[typeddict-item]
    if "modifyingProcess" in data:
        import capo_guardduty.types.process_details

        out["modifying_process"] = (
            capo_guardduty.types.process_details.deserialize_json(
                data["modifyingProcess"]
            )
        )
    if "modifiedAt" in data:
        import capo_guardduty.types.timestamp

        out["modified_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    if "scriptPath" in data:
        out["script_path"] = data["scriptPath"]
    if "libraryPath" in data:
        out["library_path"] = data["libraryPath"]
    if "ldPreloadValue" in data:
        out["ld_preload_value"] = data["ldPreloadValue"]
    if "socketPath" in data:
        out["socket_path"] = data["socketPath"]
    if "runcBinaryPath" in data:
        out["runc_binary_path"] = data["runcBinaryPath"]
    if "releaseAgentPath" in data:
        out["release_agent_path"] = data["releaseAgentPath"]
    if "mountSource" in data:
        out["mount_source"] = data["mountSource"]
    if "mountTarget" in data:
        out["mount_target"] = data["mountTarget"]
    if "fileSystemType" in data:
        out["file_system_type"] = data["fileSystemType"]
    if "flags" in data:
        import capo_guardduty.types.flags_list

        out["flags"] = capo_guardduty.types.flags_list.deserialize_json(data["flags"])
    if "moduleName" in data:
        out["module_name"] = data["moduleName"]
    if "moduleFilePath" in data:
        out["module_file_path"] = data["moduleFilePath"]
    if "moduleSha256" in data:
        out["module_sha256"] = data["moduleSha256"]
    if "shellHistoryFilePath" in data:
        out["shell_history_file_path"] = data["shellHistoryFilePath"]
    if "targetProcess" in data:
        import capo_guardduty.types.process_details

        out["target_process"] = capo_guardduty.types.process_details.deserialize_json(
            data["targetProcess"]
        )
    if "addressFamily" in data:
        out["address_family"] = data["addressFamily"]
    if "ianaProtocolNumber" in data:
        out["iana_protocol_number"] = data["ianaProtocolNumber"]
    if "memoryRegions" in data:
        import capo_guardduty.types.memory_regions_list

        out["memory_regions"] = (
            capo_guardduty.types.memory_regions_list.deserialize_json(
                data["memoryRegions"]
            )
        )
    if "toolName" in data:
        out["tool_name"] = data["toolName"]
    if "toolCategory" in data:
        out["tool_category"] = data["toolCategory"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "commandLineExample" in data:
        out["command_line_example"] = data["commandLineExample"]
    if "threatFilePath" in data:
        out["threat_file_path"] = data["threatFilePath"]
    if "fileOperation" in data:
        out["file_operation"] = data["fileOperation"]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    if "relatedFilePaths" in data:
        import capo_guardduty.types.related_file_paths_list

        out["related_file_paths"] = (
            capo_guardduty.types.related_file_paths_list.deserialize_json(
                data["relatedFilePaths"]
            )
        )
    return out
